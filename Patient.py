import cgi
class Patient:
    def __init__(self, fname, lname, patientID, status, time_waiting):
        self.fname = fname
        self.lname = lname
        self.patientID = patientID
        self.status = status
        self.time_waiting = time_waiting
    
    def __str__(self):
        return f"First name: {self.fname}\tLast Name: {self.lname}\tID: {self.patientID}\t Status: {self.status}\t Time Waiting: {self.time_waiting}"


p1 = Patient("Martha", "Martins", 222000, 1, 0)

print(p1.__str__())

form = cgi.FieldStorage()
fname = form.getvalue('fname')