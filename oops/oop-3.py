class Employee:
    def setemployee(self,eid,ename,esal): # eid,ename,esal are local variables
        self.eid = eid  # self.eid is a instace variable
        self.ename = ename # self.ename is a instance variable
        self.esal = esal # self.esal is intace variable
    def getempoyee(self):
        print(f'Employee Name : {self.eid}\nEmployee Name :{self.ename}\nEmployee Salary :{self.esal}')
emp1 = Employee() # creation object
emp1.setemployee(111,'abc',50000)
emp1.getempoyee()

emp2  = Employee()
emp2.setemployee(112,"def",60000)
emp2.getempoyee()

emp1.getempoyee()
emp2.getempoyee()