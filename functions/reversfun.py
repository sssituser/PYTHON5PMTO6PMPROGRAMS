'''
Write a program to find the reverse of a given number
num = 123  reverse = 321
'''
def reverse(num): # num = 456
    rev = 0
    while num>0: # 456>0-T 45>0-T 4>0 - t 0>0-F
        digit = num%10 # digit = 6 digit = 45%10 digit = 5 digit = 4%10 digit = 4
        rev = rev*10+digit # rev = 6 rev = 65 rev = 654
        num = num//10 # num = 456//10 num = 45  num = 45//10 num = 4//10 num = 0
    return rev

num = int(input('Enter a number : '))
print(f'{num} reverse is {reverse(num)}')