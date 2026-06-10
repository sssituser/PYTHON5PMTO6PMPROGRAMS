class Employee :# Pascal case  naming convention
    companyname = "Facebook" # class variable or static variable
    def showcompany(): # static methods(Functions) 
        print(f'Company Name : {Employee.companyname}')
    def setemployee(self,eid,ename,esal): #setemployee non static method or  instacemethod
        self.id = eid # local variables : eid ename esal
        self.name = ename # instance variables or nonstatic variables self.id sefl.name,self.sal
        self.sal = esal
    def getempoyee(self):
        print(f'Employee Id :{self.id}')
        print(f'Employee Name : {self.name}')
        print(f'Emplloyee Salary : {self.sal}')       
emp1 = Employee()    #emp1 object
emp1.setemployee(111,'abc',5000)
emp1.getempoyee()
Employee.showcompany()
   
'''
        I . variables   
            1.Class variables  or static variables
            2.local variables
            3.instance variables or non static variables
        II .Methods:
            static methods
            instance methods or non static methods  
                    :Access:      
        III . static variables or static methods can be accessed using
             className.
             
        IV. non static variables or non static methods
            Instance variabes or Instance methods 
            They can be accessed using object
        
    '''
    