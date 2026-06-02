class Employee:
    eid = 111
    ename = "abc"
    esal = 5000  # class variables , class variables can be accessed using class name
print("=============Employee Information===================")
print(f'{Employee.eid}\t{Employee.ename}\t{Employee.esal}')
Employee.eid = 1234
Employee.ename = "abcc"
Employee.esal
print(f'{Employee.eid}\t{Employee.ename}\t{Employee.esal}')
print(f'{Employee.eid}\t{Employee.ename}\t{Employee.esal}')


#Student and product