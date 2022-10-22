class Patient:
    def __init__(self, fname, lname, id, status):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.status = status
    
    def __str__(self):
        return f"First name: {self.fname}\tLast Name: {self.lname}\tID: {self.id}\t Status: {self.status}"


p1 = Patient("Martha", "Martins", 222000, 1)

print(p1.__str__())