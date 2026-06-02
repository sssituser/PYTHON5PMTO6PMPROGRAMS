class Student:
    sid = 111
    sname = 'abc'
    smarks = 600 # sid ,sname,smarks are class variables
    def showstudent(): # method
        print(f'{Student.sid}\t{Student.sname}\t{Student.smarks}')
        
Student.showstudent()