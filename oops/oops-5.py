class Test:
    compname="SSSIT" # class variable(static variable)  
    def getdata(eid,ename,esal): # eid,ename,esal local variables
        print(eid,ename,esal)
        print(f'Compay Name : {Test.compname}')
        
    def showdata():
        print(Test.compname)    
  
    def display():
        print(Test.compname)
Test.getdata(111,'abc',5000)
Test.showdata()
Test.display()

# variables class variables(staic variables) and static methods
# static variables(class variables)  and static methdos can be accessed using classname
#eid,ename , esal are local vaibles.