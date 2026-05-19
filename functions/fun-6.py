'''
write a program to find the factorial of  given number
num = 3  fact = 6
num = 4  fact = 24
'''
def fact(num):
    if num==1 or num==0:
        return 1
    else:
        return num*fact(num-1)
    
num = 3
print(f'factorial of {num} is {fact(num)}')

num = 4
print(f'factorial of {num} is {fact(num)}')

num = 5
print(f'factorial of {num} is {fact(num)}')