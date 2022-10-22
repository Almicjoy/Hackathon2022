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
        p = Patient.Patient(x[1], x[2], x[0], x[3])
        add_patient(p)

def patientExists(id):
    for patient in patient_list:
        if patient.getID() == id:
            return True
    return False

def getPatient(id):
    for patient in patient_list:
        if patient.getID() == id:
            return patient
    return "Error: No patient with this ID found"

def get_num_patients():
    return len(patient_list)  
        

create_patient()
display_queue()

# let fname = document.getElementById("fname").value
#     let lname = document.getElementById("lname").value
#     let id = document.getElementById("id").value
#     let status = document.getElementById("status").value
    
#     if (Patient.patientListSize() > 0 && !Patient.patientExists(Patient.patient_list, id)){
#         Patient.createPatient(fname, lname, id, status)
#     }
#     else {
#         alert("ID already exists");
#     }