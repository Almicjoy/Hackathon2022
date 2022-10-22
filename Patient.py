import cgi
class Patient:
    def __init__(self, fname, lname, patientID, status):
        self.fname = fname
        self.lname = lname
        self.patientID = patientID
        self.status = status
       
    
    def __str__(self):
        return f"First name: {self.fname}\tLast Name: {self.lname}\tID: {self.patientID}\t Status: {self.status}"

    def getPatientID(self):
        return self.patientID
    
    def getFname(self):
        return self.fname

    def getPatientLname(self):
        return self.lname

    def getPatientStatus(self):
        return self.status
