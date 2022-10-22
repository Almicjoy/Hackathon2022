import "Patient"

class PatientQueue {
    con
    patient_list = []

    addPatient (patient){
        patient_list.push(patient)
    }

    createPatient (fname, lname, id, status) {
        patient = Patient.Patient(fname, lname, id, status)
        addPatient(patient)
    }
}


