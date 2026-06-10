class Employee:
    companyname = 'Wipro'
    def __init__(self,eid,ename,esal): #Constructors with paraters
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def getemployee(self):
        print(f'Employee ID : {self.eid}\nEmployeeName :{self.ename}\nEmployee Salary : {self.esal}')
        print(f'Company Name : {Employee.companyname}')
 
emp1 = Employee(111,'Kiran',60000)
emp2 = Employee(112,'Raj',70000)     
emp1.getemployee()
emp2.getemployee()   