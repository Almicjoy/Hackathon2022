class Doctor:
    def __init__(self, doctorID, doctorName, status):
        self.doctorID = doctorID
        self.doctorName = doctorName
        self.status = status
    
    def __str__(self):
        return f"Doctor ID: {self.doctorID}\tDoctor Name: {self.doctorName}\tStatus: {self.status}"

d1 = Doctor(11101, True)