num1 = int(input('Enter number 1 : '))
num2 = int(input('Enter number 2 : '))
choice = int(input('1.Add\n2.Sub\n3.Mul\n4.Fdiv\n5.Div\n6.Rem\n7.Expo\nEnter your choice : '))
match choice:
    case 1:
        print(f'Sum : {num1+num2}')
    case 2:
        print(f'Sub : {num1-num2}')
    case 3:
        print(f'Mul : {num1*num2}')
    case 4:
        print(f'Fdiv : {num1//num2}') 
    case 5:
        print(f'Div : {num1/num2}')
    case 6:
        print(f'Rem : {num1%num2}')
    case 7:
        print(f'Expo : {num1**num2}')
    case _:
        print('Invalid choice : ')
        