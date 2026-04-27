num = int(input('Enter a number : '))
sum = 0
start = 1
end = num
while start<num: #1,2,4,8
    if num%start==0:
        sum = sum+start
    start = start+1
if sum==num:
    print(f'{num} is a Perfect number')
else:
    print(f'{num} is not a Perfect number')
    