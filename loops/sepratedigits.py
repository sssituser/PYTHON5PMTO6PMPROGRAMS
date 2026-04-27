'''
    Write a program to separate the digits of a number :
    456
    6,5,4
'''
num = int(input('Enter a number : ')) # num = 123
while num>0: # 123>0 -> T 12>0 -> T 1>0 -> T 0>0
    digit = num%10  #  digit = 3  digit = 12%10 digit = 2 digit = 1%10 digit = 1
    print(digit) # 3 2 1
    num = num//10 #  num = 123//10 num = 12//10  num = 1//10 num = 0