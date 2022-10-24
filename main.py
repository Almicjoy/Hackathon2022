import sqlite3
import WaitingQueue
import Patient

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


    def __init__(self, patient_fname, patient_lname, patient_id, status, position):
        self.id = patient_id
        self.fname = patient_fname
        self.lname = patient_lname
        self.status = status
        self.position = position


class Doctors_DB(db.Model):
    id = db.Column('dr_id', db.Integer, primary_key=True)
    name = db.Column('dr_name', db.String(20))
    status = db.Column('dr_status', db.Boolean)

    def __init__(self, dr_id, dr_name, dr_status):
        self.id = dr_id
        self.name = dr_name
        self.status = dr_status


class Rooms_DB(db.Model):
    number = db.Column('room_id', db.Integer, primary_key=True)
    room_status = db.Column('room_status', db.Boolean)

    def __init__(self, room_number, room_status):
        self.number = room_number
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
            # if db.session.query.(Patients_DB.id).filter(Patients_DB.id == retrieved_id).count() > 0:
            if Patients_DB.query.filter_by(id = retrieved_id).count() > 0:
                Patients_DB.query.filter_by(id = retrieved_id).update(dict(status = 0))
                Patients_DB.query.filter_by(id = retrieved_id).update(dict(position = WaitingQueue.get_pos(retrieved_id)))
                db.session.commit()
                flash('ID already exists in Database. Patient added to Waiting Queue')
                
            else:
                patient = Patients_DB(request.form['fname'], request.form['lname'], request.form['id'], 0, WaitingQueue.get_pos(retrieved_id))
                db.session.add(patient)
                db.session.commit()
                flash('Record was successfully added. Patient added to Waiting Queue')
            
            return redirect(url_for('show_waiting'))
    else:
        return render_template('index.html')

def move_to_ready():
    if 'ready_button' in request.form:
        patient = WaitingQueue.remove_patient()
        Patients_DB.query.filter_by(id = patient.getPatientID).update(dict(status = 1))
        Patients_DB.query.filter_by(status = 0).update(dict(position = Patients_DB.position - 1))
        Patients_DB.query.filter_by(id = patient.getPatientID).update(dict(position = ReadyQueue.get_pos(patient.getPatientID)))
        ReadyQueue.add_patient(patient)
        db.session.commit()
    
@app.route('/')
def show_waiting():
    return render_template('show_queues.html', patients = Patients_DB.query.filter_by(status = 0).all())

@app.route('/')
def show_ready():
    return render_template('show_queues.html', ready_patients = Patients_DB.query.filter_by(status = 1).all())

def show_in_progress():
    return render_template('show_queues.html', ready_patients = Patients_DB.query.filter_by(status = 2).all())

def show_on_hold():
    return render_template('show_queues.html', ready_patients = Patients_DB.query.filter_by(status = 3).all())

def show_checked_out():
    return render_template('show_queues.html', ready_patients = Patients_DB.query.filter_by(status = 4).all())

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
