class Patient {
    constructor (fname, lname, id, status) {
        this.fname = fname
        this.lname = lname
        this.id = id
        this.status = status
    }

    get fname () {
        return this.fname
    }
    get lname () {
        return this.lname
    }
    get id () {
        return this.id
    }
    get status () {
        return this.status
    }

    patient_list = []

    addPatient (patient){
        patient_list.push(patient)
    }

    createPatient (fname, lname, id, status) {
        let patient = Patient(fname, lname, id, status)
        addPatient(patient)
    }
    patientListSize() {
        return this.patient_list.length
    }
    patientExists(p, id) {
        for (var i = 0; i < this.patientListSize(); i++) {
            if (p.getID() == id){
                return true
            }
        }
        return false
    }
    

}

