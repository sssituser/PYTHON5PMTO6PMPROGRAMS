class Student:
    def __init__(self): # Defualt Constructor
        print("Iam constructor")
        self.sid = 111
        self.sname = "abc"   
    def get(self):
        print(self.sid,self.sname)

s1 = Student()
s2 = Student()
s3 = Student()
s1.get()
s2.get()
s3.get()