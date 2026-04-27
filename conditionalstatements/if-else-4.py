import getpass
username = input('Enter User Name : ')
password = getpass.getpass('Enter Password   : ')
if (username=='admin' or username =="Admin") and password=="1234":
    print('Login Success...,Your are Welcome ')
else:
    print('Invalid Credentials...')
    
    