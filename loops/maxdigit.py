num = int(input('Enter a number : '))  #765
max = num%10 # max = 765%10   max = 5
while num>0: # 765>0 76>0-T 7>0-T 0>0
    digit = num%10 # digit = 765%10 digit = 5 digit = 76%10 digit = 6 digit = 7%10 digit = 7
    if digit>max:
        max = digit # max = 6 max = 7
    num = num//10 # num = 765//10 num = 76//10 num = 7//10 num = 0
print(f'Max digit is :{max}')
        
        