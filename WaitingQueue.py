import Patient
import sqlite3

patient_list = []

def add_patient(patient):
    patient_list.append(patient)

def remove_patient():
    patient = patient_list.pop(0)
    return patient

def display_queue():
    for patient in patient_list:
        print(patient.__str__())


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

def get_pos(id):
    for i, patient in enumerate(patient_list):
        if patient.getPatientID() == id:
            j = i + 1
            return j
    return "Error: No patient with this ID found"

def get_num_patients():
    return len(patient_list)  

def is_empty():
    if bool(patient_list):
        return False
    else:
        return True     


