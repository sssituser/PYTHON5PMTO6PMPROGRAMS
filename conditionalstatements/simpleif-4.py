num1 = int(input('Enter Number 1 : '))
num2 = int(input('Enter Number 2 : '))
choice =int(input('1.Add\n2.Sub\n3.Mul\n4.Div\n5.Rem\n6.Expo\nEnter Your choice :'))
if choice==1:
    print(f'sum is : {num1+num2}')
if choice==2:
    print(f'sub is : {num1-num2}')
if choice==3:
    print(f'mul is : {num1*num2}')
if choice==4:
    print(f'Quo is : {num1//num2}')
if choice==5:
    print(f'Rem is : {num1%num2}')
if choice ==6:
    print(f'{num1} To the Power of  {num2} is {num1**num2}')
if choice>6 or choice<1:
    print(f'Enter Valid choice')





