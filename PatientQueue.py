import Patient
import main
import sqlite3

patient_list = []

def addPatient(patient):
    patient_list.append(patient)

# def removePatient():
#     p = patient_list[0]
#     patient_list.pop(0)
#     return p




def display_queue():
    for patient in patient_list:
        print(patient.__str__())

def create_patient():
    connect = sqlite3.connect("instance/hospital.db")
    cursor = connect.cursor()
    for x in cursor.execute("SELECT * FROM patients_db"):
        print(x)
        # p = Patient.Patient(fname, lname, id, status)

# p = removePatient()
# pri

create_patient()