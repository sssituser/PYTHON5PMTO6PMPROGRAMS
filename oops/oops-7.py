class Employee:
    cname = "SSSIT PVT LTD" # class variable or static variable
    def setemployee(self,eid,ename,esal): # non static method
        self.id = eid  # eid local var   self.id non-static or instance va
        self.name = ename #  ename local self.name non static or intance var
        self.sal = esal # esal local self.sal non-static var or instance
    def getemployee(self): # non - static  ro Instance method
        print(f'Employee ID     : {self.id}')
        print(f'Employee Name   : {self.name}')
        print(f'Employee Salary : {self.sal}')
        print(f'Company Name    : {self.cname}')
emp1 = Employee()
emp1.setemployee(111,'Latha',50000)
emp2 = Employee()
emp2.setemployee(112,'Sindhu',50000)

emp1.getemployee()
emp2.getemployee()