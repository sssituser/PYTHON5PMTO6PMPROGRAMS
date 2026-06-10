class Employee:
    def __init__(self,eid,ename,esal): 
        self.__eid = eid
        self.__ename = ename
        self.__esal = esal
    def getemployee(self):
        print(f'Employee ID : {self.__eid}\nEmployee Name :{self.__ename}\nEmployee Salary : {self.__esal}')
emp1 = Employee(111,"abc",5000)
emp1.getemployee()
