class Employee:
    companyname = "TCS"
    def setemployee(self,eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def getemployee(self):
        print(f'Employee ID : {self.eid}\nEmployee Name : {self.ename}\nEmployee Salary : {self.esal}')
        print(f'Company Name : {Employee.companyname}')

print("==================Employee 1 Object============")

emp1 = Employee()
emp1.setemployee(111,'abc',60000)
emp1.getemployee()

print("==================Employee 2 Object========")

emp2 = Employee()
emp2.setemployee(112,'def',50000)
emp2.getemployee()
    
    