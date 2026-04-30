'''
Write a program to generate numbers from 1 to the given numeber.

num = 5   res = 1 2 3 4 5
num = 9   res = 1 2 3 4 5 6 7 8 9
'''
num = int(input('Enter a number : ')) # 5
for val in range(1,num+1,2):
    print(val,end="  ")
    
    
# range(start,endvalue) 