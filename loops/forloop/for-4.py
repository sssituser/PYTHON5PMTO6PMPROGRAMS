'''
Write program to generate multiplication tables for the given number from 1.
num = 5
1 x 1 = 1

'''
num = int(input('Enter number : '))
for i in range(1,num+1):
    print("=======================")
    for j in range(1,11):
        print(f'{i} x {j} = {i*j}')
   
   
   
'''
    num = 5
    1
    1   2
    1   2   3
    1   2   3   4
    1   2   3   4   5
      
    
    1
    2   2
    3   3   3   
    4   4   4   4
    5   5   5   5   5
    
    1
    2   3
    4   5   6
    7   8   9   10
    11  12  13  14   15
   
  '''
   