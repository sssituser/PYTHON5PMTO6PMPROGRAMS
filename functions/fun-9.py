'''
Find the max digit of a given number
num = 345   maxdigit is = 5
num = 876   maxdigit is = 8
'''
def getmaxdigit(num): # num = 345
    max = num%10  # max = 345%10 max = 5 
    while num>0: # 345>0-T 34>0 3>0
        digit = num%10 # digit = 5 digit = 34%10 digit = 4 digit = 3%10 digit = 3
        if digit > max:
            max = digit
        num = num//10 # num = 345//10 num = 34//10 num = 3//10 num = 0
    return max

print(getmaxdigit(234))
print(getmaxdigit(876))
print(getmaxdigit(345))