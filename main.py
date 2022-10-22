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


    def __init__(self, patient_fname, patient_lname, patient_id):
        self.id = patient_id
        self.fname = patient_fname
        self.lname = patient_lname


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


@app.route('/', methods=['GET', 'POST'])
def show_home():
    if request.method == 'POST':
        patient = Patients_DB(request.form['fname'], request.form['lname'],
                              request.form['id'])

        db.session.add(patient)
        db.session.commit()

        flash('Success')

        return redirect(url_for('show_prof'))
    else:
        return render_template('index.html')


@app.route('/list_all', methods=['GET', 'POST'])
def show_prof():
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
