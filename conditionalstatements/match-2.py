num1 = int(input('Enter number 1 : '))
num2 = int(input('Enter number 2 : '))
choice = input('+\n-\n*\n//\n/\n%\n**\nEnter your choice : ')
match choice:
    case "+":
        print(f'Sum : {num1+num2}')
    case "-":
        print(f'Sub : {num1-num2}')
    case "*":
        print(f'Mul : {num1*num2}')
    case "//":
        print(f'Fdiv : {num1//num2}') 
    case "/":
        print(f'Div : {num1/num2}')
    case "%":
        print(f'Rem : {num1%num2}')
    case "**":
        print(f'Expo : {num1**num2}')
    case _:
        print('Invalid choice : ')
        