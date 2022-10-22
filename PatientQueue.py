import Patient
import sqlite3

patient_list = []

def add_patient(patient):
    patient_list.append(patient)

def removePatient():
    patient_list.pop(0)

def display_queue():
    for patient in patient_list:
        print(patient.__str__())

def create_patient():
    connect = sqlite3.connect("instance/hospital.db")
    cursor = connect.cursor()
    for x in cursor.execute("SELECT * FROM patients_db"):
        print(x[2])
        p = Patient.Patient(x[1], x[2], x[0], 0)
        add_patient(p)


def get_num_patients():
    return len(patient_list)  
        

create_patient()
display_queue()