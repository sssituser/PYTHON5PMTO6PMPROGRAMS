num = int(input('Enter number : ')) # num = 8
start = 1
end = num
while start<=end: #1<=8-T 2<=8-T 3<=8-T 4<=8-T 5<=8-T 6<=8-T 7<=8-T 8<=8-T 9<=8-F
    if num%start == 0:
        print(start,end=" ")# 1,2,4,8
    start = start+1
    
        