'''
Write a program to count the digits of a given number.
num = 5678   digitCount = 4
'''
def digitcount(num):#350
    count = 0
    while num>0: #350>0->True 35>0-T 3>0-T 0>0-F
        digit = num%10 # digit 350%10 digit = 0 digit = 35%10 digit = 5 digit = 3%10 digit = 3
        count = count+1 # count = 1 count = 2 count = 3
        num  = num//10 # num = 350//10 num = 35 num = 35//10 num = 3//10 num = 0
    return count
num = int(input('Enter a number : '))

print(f'{num} has {digitcount(num)} digits')

