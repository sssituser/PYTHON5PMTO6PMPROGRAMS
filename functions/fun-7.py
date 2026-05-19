'''
Write program to swap given two numbers
'''

def swap1(num1,num2):
    print(f'Before swaping the values num1 = {num1}\tnum2 = {num2}')
    copy = num1
    num1 =  num2
    num2 = copy
    print(f'After swaping the values num1 = {num1}\tnum2 = {num2}')

def swap2(num1,num2):
    print(f'Before swaping the values num1 = {num1}\tnum2 = {num2}')
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    print(f'After swaping the values num1 = {num1}\tnum2 = {num2}')
def swap3(num1,num2):
    print(f'Before swaping the values num1 = {num1}\tnum2 = {num2}')
    num1,num2 = num2,num1
    print(f'After swaping the values num1 = {num1}\tnum2 = {num2}')
    
print("Swaping numbers using swap1 functions")
num1 = 10
num2 = 20
swap1(num1,num2)
print("Swaping numbers using swap2 functions")
num1 = 10
num2 = 20
swap2(num1,num2)
print("Swaping numbers using swap3 functions")    
num1 = 10
num2 = 20
swap3(num1,num2)
