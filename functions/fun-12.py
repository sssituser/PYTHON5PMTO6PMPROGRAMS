'''
Write a program to find the sum of the digits of given number
num = 123 sum = 1+2+3 => 6
'''
def digitsum(num):
    sum = 0
    while num>0:
        digit = num%10
        sum = sum + digit
        num = num//10
    return sum

num = int(input('Enter a number : '))
print(f'{num} digits sum is {digitsum(num)}')