import Patient

patient_list = []

def addPatient(patient):
    patient_list.append(patient)

def removePatient():
    p = patient_list[0]
    patient_list.pop(0)
    return p



addPatient(p)
addPatient(p2)

def display_queue():
    for patient in patient_list:
        print(patient.__str__())

def create_patient(fname, lname, id, status):
    p = Patient.Patient(fname, lname, id, status)