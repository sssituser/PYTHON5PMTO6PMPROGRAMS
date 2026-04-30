'''
num = 5
1
1   2
1   2   3
1   2   3   4
1   2   3   4   5
rows-5
ro-1   1 col    
ro-2   1 col 2col
ro-3   1 col 2col 3col
ro-4   1 
'''
num = int(input('Enter a number : '))#5
k = 1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(k,end="\t")
        k = k+1
    print()

