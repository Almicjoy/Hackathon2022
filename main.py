from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///hospital.db"

db = SQLAlchemy(app)

statuses = {0: 'waiting', 1: 'ready', 2: 'in_progress', 3: 'on_hold', 4: 'checked_out'}


class Patient_DB():
    id = db.Column('patient_id', db.Integer, primary_key=True)
    name = db.Column('patient_name', db.String(25))
    patient_status = db.Column('patient_status', db.Integer)
    time_waiting = db.Column('time_waiting', db.String(8))

    def __init__(self, patient_id, patient_name, patient_status, time_waiting):
        self.id = patient_id
        self.name = patient_name
        self.patient_status = patient_status
        self.time_waiting = time_waiting


class Doctor_DB():
    id = db.Column('dr_id', db.Integer, primary_key=True)
    name = db.Column('dr_name', db.String(20))
    status = db.Column('dr_status', db.Boolean)

    def __init__(self, dr_id, dr_name, dr_status):
        self.id = dr_id
        self.name = dr_name
        self.status = dr_status

class Room_DB():
    number = db.Column('room_id', primary_key=True)
    room_status = db.Column('room_status', db.Boolean)

    def __init__(self, room_number, room_status):
        self.number = room_number
        self.room_status = room_status

class Appointment_ID():
    patient_id = db.Column('patient_id', db.Integer)
    dr_id = db.Column('dr_id', db.Integer)
    room_number = db.Column('room_number', db.Integer)
    desc = db.Column('description', db.String(500))
    app_id = db.Column('app_id', db.Integer)

    def __init__(self, p_id, dr_id, room_number, desc, app_id):
        self.patient_id = p_id
        self.dr_id = dr_id
        self.room_number = room_number
        self.desc = desc
        self.app_id = app_id




@app.route('/')
def show_home():
    return render_template('index.html', name="Aaliyah")


@app.route('/profile')
def show_prof():
    pass


if __name__ == '__main__':
    app.run(debug=True)
