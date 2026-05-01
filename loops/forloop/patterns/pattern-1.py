'''
num = 5
1
1   2
1   2   3
1   2   3   4
1   2   3   4   5
row - 1    1
row - 2    1    2
row - 3    1    2   3
row - 4    1    2   3   4
row - 5    1    2   3   4   5



'''
num = int(input('Enter a number : '))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(f'{i}',end="  ")
    print()
