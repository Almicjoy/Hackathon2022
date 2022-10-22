class Doctor:
    def __init__(self, doctorID, status):
        self.doctorID = doctorID
        self.status = status
    
    def __str__(self):
        return f"Doctor ID: {self.doctorID}\tStatus: {self.status}"

d1 = Doctor(11101, True)