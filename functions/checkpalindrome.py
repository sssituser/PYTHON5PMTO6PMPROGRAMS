'''
Write a program check given number is Palindrome or not
'''
s = 'abc'
def reverse(num): # num = 123
    rev = 0
    while num>0: # 456>0-T 45>0-T 4>0 - t 0>0-F
        digit = num%10 # digit = 6 digit = 45%10 digit = 5 digit = 4%10 digit = 4
        rev = rev*10+digit # rev = 6 rev = 65 rev = 654
        num = num//10
    return rev

def ispalinrome(num): #123
    return num == reverse(num)

print(ispalinrome(123))