import WaitingQueue
import Patient
import Room

from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///hospital.db"
app.config['SECRET_KEY'] = "12345"

db = SQLAlchemy(app)

statuses = {0: 'waiting', 1: 'ready', 2: 'in_progress', 3: 'on_hold', 4: 'checked_out'}


class Patients_DB(db.Model):
    id = db.Column('patient_id', db.Integer, primary_key=True)
    fname = db.Column('patient_fname', db.String(25))
    lname = db.Column('patient_lname', db.String(25))
    status = db.Column('status', db.Integer)
    position = db.Column('position', db.Integer)
    room = db.Column('room', db.Integer)


    def __init__(self, patient_fname, patient_lname, patient_id, status, position, room):
        self.id = patient_id
        self.fname = patient_fname
        self.lname = patient_lname
        self.status = status
        self.position = position
        self.room = room


class Doctors_DB(db.Model):
    id = db.Column('dr_id', db.Integer, primary_key=True)
    name = db.Column('dr_name', db.String(20))
    status = db.Column('dr_status', db.Boolean)

    def __init__(self, dr_id, dr_name, dr_status):
        self.id = dr_id
        self.name = dr_name
        self.status = dr_status


class Rooms_DB(db.Model):
    room_number = db.Column('room_id', db.Integer, primary_key=True)
    room_status = db.Column('room_status', db.Boolean)

    def __init__(self, room_number, room_status):
        self.room_number = room_number
        self.room_status = room_status


class Appointments_ID(db.Model):
    patient_id = db.Column('patient_id', db.Integer)
    dr_id = db.Column('dr_id', db.Integer)
    room_number = db.Column('room_number', db.Integer)
    desc = db.Column('description', db.String(500))
    app_id = db.Column('app_id', db.Integer, primary_key=True)

    def __init__(self, p_id, dr_id, room_number, desc, app_id):
        self.patient_id = p_id
        self.dr_id = dr_id
        self.room_number = room_number
        self.desc = desc
        self.app_id = app_id


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['fname'] or not request.form['lname'] or not request.form['id']:
            flash('Please enter all the fields', 'error')
        else:
            patient = Patient.Patient(request.form['fname'], request.form['lname'], request.form['id'], 0)
            WaitingQueue.add_patient(patient)
            retrieved_id = request.form['id']
            if Patients_DB.query.filter_by(id = retrieved_id).count() > 0:
                Patients_DB.query.filter_by(id = retrieved_id).update(dict(status = 0))
                Patients_DB.query.filter_by(id = retrieved_id).update(dict(position = WaitingQueue.get_pos(retrieved_id)))
                db.session.commit()
                flash('ID already exists in Database. Patient added to Waiting Queue')
                
            else:
                patient = Patients_DB(request.form['fname'], request.form['lname'], request.form['id'], 0, WaitingQueue.get_pos(retrieved_id), 0)
                db.session.add(patient)
                db.session.commit()
                flash('Record was successfully added. Patient added to Waiting Queue')
            
            return redirect(url_for('show_waiting'))
    else:
        return render_template('index.html')
    
@app.route('/addrooms', methods=['GET', 'POST'])
def room():
    if request.method == 'POST':
        room_num = request.form['roomnum']
        if Rooms_DB.query.filter_by(room_number = room_num).count() > 0:
            flash('Room already exists in database')
        else:
            room = Rooms_DB(room_num, 0)
            db.session.add(room)
            db.session.commit()
            flash("Room was successfully added to database")
        
        return redirect(url_for('show_waiting'))
    else:
        return render_template('add_rooms.html')

@app.route('/', methods=['GET', 'POST'])
def show_waiting():
    if request.method == 'POST':
        if request.form.get('ready_button') == 'Ready':
            if WaitingQueue.is_empty():
                flash('Queue is empty!')
            elif Rooms_DB.query.filter_by(room_status = 0).count() == 0:
                flash('No Rooms Available')
            else:
                patient = WaitingQueue.remove_patient()
                ReadyQueue.add_patient(patient)
                Patients_DB.query.filter_by(id = patient.getPatientID()).update(dict(status = 1))
                room = Rooms_DB.query.filter_by(room_status = 0).first()
                Patients_DB.query.filter_by(id = patient.getPatientID()).update(dict(room = room.room_number))
                Rooms_DB.query.filter_by(room_number = room.room_number).update(dict(room_status = 1))
                Patients_DB.query.filter_by(status = 0).update(dict(position = Patients_DB.position - 1))
                Patients_DB.query.filter_by(id = patient.getPatientID()).update(dict(position = 0))
                db.session.commit()
        
        if request.form.get('pos') == '+':
                pos = request.form['position']
                int_pos = int(pos)
                if int_pos == 1:
                    flash('Patient is at the top of the queue')
                else:
                    WaitingQueue.patient_list[int_pos-2], WaitingQueue.patient_list[int_pos-1] = WaitingQueue.patient_list[int_pos-1], WaitingQueue.patient_list[int_pos-2]
                    for patient in WaitingQueue.patient_list:
                        Patients_DB.query.filter_by(id = patient.getPatientID()).update(dict(position = WaitingQueue.get_pos(patient.getPatientID())))
                        db.session.commit()

        if request.form.get('pos') == '-':
                pos = request.form['position']
                int_pos = int(pos)
                if int_pos == WaitingQueue.get_num_patients():
                    flash('Patient is at the bottom of the queue')
                else:
                    WaitingQueue.patient_list[int_pos-1], WaitingQueue.patient_list[int_pos] = WaitingQueue.patient_list[int_pos], WaitingQueue.patient_list[int_pos-1]
                    for patient in WaitingQueue.patient_list:
                        Patients_DB.query.filter_by(id = patient.getPatientID()).update(dict(position = WaitingQueue.get_pos(patient.getPatientID())))
                        db.session.commit()
    
    return render_template('show_queues.html', waiting_patients = waiting(), ready_patients = ready(), rooms = get_rooms())

def waiting():
    waiting_patients = Patients_DB.query.filter_by(status = 0).order_by(Patients_DB.position)
    return waiting_patients

def ready():
    ready_patients = Patients_DB.query.filter_by(status = 1).order_by(Patients_DB.position)
    return ready_patients

def in_progress():
    in_progress_patients = Patients_DB.query.filter_by(status = 2).all()
    return in_progress_patients

def on_hold():
    on_hold_patients = Patients_DB.query.filter_by(status = 3).all()
    return on_hold_patients

def checked_out():
    checked_out_patients = Patients_DB.query.filter_by(status = 4).all()
    return checked_out_patients
    
def get_rooms():
    rooms = Rooms_DB.query.filter_by(room_status = 0).all()
    return rooms

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
