import Patient

patient_list = []

def addPatient(patient):
    patient_list.append(patient)

def removePatient():
    p = patient_list[0]
    patient_list.pop(0)
    return p

p = Patient.Patient("Some", "Dude", 22222, 0, 0)
p2 = Patient.Patient("Martha", "Martins", 34343, 0, 0)

addPatient(p)
addPatient(p2)

def display_queue():
    for patient in patient_list:
        print(patient.__str__())