class Student:
    collagename = "Aruns Collage" # class variable
    def setstudent(self,sid,sname,smarks): #instance method or non static
        self.id = sid # sid local is a variable self.id instance
        self.name = sname #sname is a local variable self.name instance variable
        self.marks = smarks # smarks a local self.marks instance variale
    def getstudent(self): 
        print(f"Student ID :{self.id}\nStudent Name : {self.name}\nStudent Marks : {self.marks}")
        print(f'CollegeName : {Student.collagename}')
        
s1 = Student()    
s1.setstudent(111,"Sindhuja",800)
s1.getstudent()

s2 = Student()
s2.setstudent(112,"Latha",800)
s2.getstudent() 
    