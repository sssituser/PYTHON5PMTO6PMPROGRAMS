num1 = int(input('Enter number 1 : '))
num2 = int(input('Enter number 2 : '))
choice = input('Add\nSub\nMul\nFdiv\nDiv\nRem\nExpo\nEnter your choice : ')
match choice:
    case "Add":
        print(f'Sum : {num1+num2}')
    case "Sub":
        print(f'Sub : {num1-num2}')
    case "Mul":
        print(f'Mul : {num1*num2}')
    case "Fdiv":
        print(f'Fdiv : {num1//num2}') 
    case "Div":
        print(f'Div : {num1/num2}')
    case "Rem":
        print(f'Rem : {num1%num2}')
    case "Expo":
        print(f'Expo : {num1**num2}')
    case _:
        print('Invalid choice : ')
        