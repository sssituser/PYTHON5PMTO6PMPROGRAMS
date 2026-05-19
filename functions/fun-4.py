'''
Recursive function : The function which calling function is called 
recursive function.

Create an application which calculates sum of n numbers.
Example : num = 5   sum  = 1+2+3+4+5 => 15
'''
def sum(num):
    if num==1:
        return 1
    else:
        return num+sum(num-1)
    
'''
sum(5)=>5+sum(4)=>4+sum(3)=>3+sum(2)=>2+sum(1)
sum(5)=>5+sum(4)=>4+sum(3)=>3+sum(2)=>2+1
sum(5)=>5+sum(4)=>4+sum(3)=>3+3
sum(5)=>5+sum(4)=>4+6
sum(5)=>5+10
sum(5)=>15
'''
   
    
num = 5
res = sum(num) # calling the function
print(f'Sum of {num} numbers is : {res}')

print(sum(6))
print(sum(10))