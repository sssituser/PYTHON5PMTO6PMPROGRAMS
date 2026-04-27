'''
Write a progrm to find the sum of the digits of a given number
num = 654 sum = 15
num = 123 sum = 6
'''
num = int(input('Enter a number : '))  #456
sum = 0 # sum = 0
while num>0: # 456>0-> T 45>0->T 4>0->T 0>0
    digit = num%10 # digit = 456%10 digit = 6 digit = 45%10 digit = 5 digit = 4%10 digit = 4
    sum = sum + digit # sum = 6 sum = 11 sum = 15
    num = num//10 # num = 456//10 num = 45//10  num = 4//10 num = 0
print(f'sum of the digits of a  given number is {sum}')