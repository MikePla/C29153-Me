print('Привет это калькулятор')
d = 0
restart1 = 1

while restart1 == 1:
    a = int(input('Ведите первое значение : '))
    b = int(input('Ведите второе начение : '))
    c = input('Ведите какое действие \n[+]-сумма\n[/]-деление\n[*]-произведение\n[-]-разница\n[**]-степень\n[1]-замена первого числа\n Выбор : ')
    if c == '1':
        restart1 = 1
    if c == ('+'):
        d = a + b
        print('Ответ :', d)
        restart1 = int(input('Заново 1-Да/0-Нет :'))
    elif c == ('/'):
        if b == 0:
            print('Введите другие число')
            restart1 == 1
        else:
            d = a / b
            print('Ответ :', d)
            restart1 = int(input('Заново 1-Да/0-Нет :'))
    elif c == ('*'):
        d = a * b
        print('Ответ :', d)
        restart1 = int(input('Заново 1-Да/0-Нет :'))
    elif c == ('-'):
        d = a - b
        print('Ответ :', d)
        restart1 = int(input('Заново 1-Да/0-Нет :'))
    elif c == ('**'):
        d = a ** b
        print('Ответ :', d)
        restart1 = int(input('Заново 1-Да/0-Нет :'))
    elif c == '1':
        d = 0
    else:
        print('Неверное условие')
        restart1 = 1
print("Пока")
