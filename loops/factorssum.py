num = int(input('Enter a number : '))
sum = 0
start = 1
end = num
while start<=num: #1,2,4,8
    if num%start==0:
        sum = sum+start
    start = start+1
print(f'{num} sum of the factors {sum}  factors')
    