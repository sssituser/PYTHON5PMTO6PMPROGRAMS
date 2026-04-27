'''
Write a program to count the digits of a given number
num = 123 Digits = 3
num = 456 Digit = 3
'''
num = int(input('Enter number : ')) # 234
count = 0
while num>0:# 234>0-T 23>0-T 2>0-T 0>0
    digit = num%10 # digit = 234%10 digit = 4 digit = 23%10  digit = 3 digit = 2%10 digit = 2
    count = count+1 # count = 1 count = 2 count = 3
    num = num//10 # num = 234//10 num = 23//10 num = 2//10 num = 0
print(f'No of Digits present in the given number is : {count}')