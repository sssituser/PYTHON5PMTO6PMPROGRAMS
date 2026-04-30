'''
Write program to generate a multiplication table for the given number ?
num = 5
5 x 1 = 5

5 x 10 = 50
'''
num = int(input('Enter a number : ')) # num = 5
for i in range(1,11):
    print(f'{num} x {i} = {num*i}')
