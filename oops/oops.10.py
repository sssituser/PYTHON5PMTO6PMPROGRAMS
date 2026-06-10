class Doctor:
    hpname = "Yeshoda" # class variable or static varialbes
    def __init__(self,did,dname,ddesc): # constructor with parameters
        self.did = did
        self.dname = dname
        self.ddesc = ddesc
    def show(self):
        print(f'Doctor ID : {self.did}\nDoctor Name : {self.dname}\nDescription : {self.ddesc}')
        print(f'Hospital Name : {Doctor.hpname}')
d1 = Doctor(111,"Ram","Gen.Phy")
d2 = Doctor(112,"Preeti","Nero Phy")
d1.show()
d2.show()
        