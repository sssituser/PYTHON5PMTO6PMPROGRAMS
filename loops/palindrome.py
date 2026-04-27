num = int(input('Enter a number  : ')) # 123  res 321
copy = num
rev = 0
while num>0: # 123>0-T 12>0-T 1>0-T 0>0-F
    digit = num%10 # digit = 123%10 digit = 3 digit = 12%10 digit = 2 digit = 1%10 digit = 1
    rev = rev*10+digit # rev =3 rev = 32 rev = 321
    num = num//10# num =123//10 num = 12//10 num = 1//10 num = 0
if copy == rev:
    print(f'{copy} is a Palindrome number')
else:
    print(f'{copy} is not a Palindrome number')