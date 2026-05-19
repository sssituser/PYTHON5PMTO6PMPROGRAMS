'''
Write a program (Create an application) which separeates the digits
of a given number
num = 345   res = 5,4,3
num = 456   res = 4,5,6
'''
def separatedigits(num): # 345
    while num>0: # 345>0 34>0 3>0 0>0
        digit = num%10 # digit = 345%10 digit = 5 digit = 34%10  digit = 4 digit = 3%10 digit = 3
        print(digit,end="\t") # 5 ,4 , 3
        num = num//10  # num = 345/10 num = 34//10 num = 3//10 num = 0
separatedigits(345)

# write a program to find the sum of digits of given number 345  sum = 12
# num = 123 sum = 6
