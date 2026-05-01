'''
num = 5
1
1   2
1   2   3
1   2   3   4
1   2   3   4   5
1   2   3   4
1   2   3
1   2
1
'''
num = int(input('Enter a number : '))#num = 5
k = 65
for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(k),end="  ") # chr is a function which can convert ASCII into alphabet A - 65
        k = k+1
    print()
for i in range(num,0,-1):
    for j in range(1,i):
        print(chr(k),end="  ")
        k = k+1
    print()
        
    
