def calculator():
    a = int(input('Введите число A\n'))
    operator = input('Введите знак операции (+, -, *, /) или z (нижний регистр) для выхода\n')
    b = int(input('Введите число B\n'))
    oplist = ['+', '-', '*', '/']
    if operator == 'z':
        quit()
    elif operator not in oplist:
        print('Введите знак из списка!')
    elif operator == oplist[0]:
        print(f'Результат {a} + {b} = {a + b}')
        return calculator()
    elif operator == oplist[1]:
        print(f'Результат {a} - {b} = {a - b}')
        return calculator()
    elif operator == oplist[2]:
        print(f'Результат {a} * {b} = {a * b}')
        return calculator()
    elif operator == oplist[3]:
        print(f'Результат {a} / {b} = {a / b}')
        return calculator()
    else:
        pass


calculator()