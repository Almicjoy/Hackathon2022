import "Patient"

const patient_list = []

function addPatient (patient){
    patient_list.push(patient)
}

function createPatient (fname, lname, id, status) {
    patient = Patient.Patient(fname, lname, id, status)
    addPatient(patient)
}

createPatient("Sally", "Sand", 2222, 0)
print(patient_list)