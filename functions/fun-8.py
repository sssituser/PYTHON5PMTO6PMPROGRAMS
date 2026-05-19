'''
lets assume x is number and is divisble by y , remainder 0
8%2=>0   
5%2=>1
5//2 => 2
Write a program to check given number is factor or not
'''
def isfactor(x,y):
    return x%y==0    

print(isfactor(4,2))
print(isfactor(5,2))


