import MySQLdb as PDBC
con = PDBC.connect(host="localhost",user="root",password="root",db="lathadb")
cur = con.cursor()

while True:
    choice = int(input("1.Insert\n2.Update\n3.Find\n4.FindAll\n5.Delete\nEnter Your choice : "))
    match choice:
        case 1:
            id = int(input('Enter ID : '))
            name = input('Enter Name : ')
            sal = int(input("Enter Salary :"))
            cur.execute("insert into employee values(%s,%s,%s)",(id,name,sal))
            con.commit()
            print("Record Inserted......")
        case 2: 
            id = int(input('Enter ID : '))
            name = input('Enter Name : ')
            sal = int(input("Enter Salary :"))
            cur.execute("update employee set ename=%s,esal = %s where eid = %s ",(name,sal,id))
            con.commit()
            print("Record updated......")
        case 3:
            id = int(input('Enter ID : '))
        
            cur.execute("select * from employee where eid = %s",(id,))
            emp = cur.fetchone()
            if emp:
                print(f"Employee info :{emp}")
            else:
                print("Employee Not Found")
        case 4:
            cur.execute("select * from employee")
            employees = cur.fetchall()
            for emp in employees:
                print(emp)
        case 5:
            id = int(input('Enter id to delete : '))
            cur.execute("delete from employee where eid = %s",(id,))
           
            print("Employee Deleted")
           
            