num = int(input('Enter a number : '))
count = 0
start = 1
end = num
while start<=num:
    if num%start==0:
        count=count+1
    start = start+1
print(f'{num} has {count}  factors')
    