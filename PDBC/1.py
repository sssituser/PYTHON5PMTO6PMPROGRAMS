import MySQLdb as dbc
id = int(input("Enter Employee ID : "))
name = input("Enter Employee Name : ")
sal = int(input('Enter Employee Salary : '))
# PDBC Codecls
con = dbc.connect( host='localhost', user='root',  password='root',   db='lathadb')
cur = con.cursor()
cur.execute("insert into employee values(%s,%s,%s)",(id,name,sal))
con.commit()
print("Record Inserted")

