answer=0
print('Ты попал на тест тут всего 5 вопросов')
#1
print("1)В каком году ты живеш?\n\ta)2021\n\tб)2023\n\tв)2020\n\tг)2022")
a1=input('Ведите ответ:')
if a1==("г"):
    print('Правильно')
    answer=2.4+answer
else:
    print('Неправильно')
print("Ваш бал стал =",answer)
#2
print("2)В каком году была вторая мировая?\n\ta)1049\n\tб)1949\n\tв)1939\n\tг)1941")
a2=input('Ведите ответ:')
if a2==("в"):
    print('Правильно')
    answer=2.4+answer
else:
    print('Неправильно')
print("Ваш бал стал =",answer)
#3
print("3)Как зовут нашего учителя по Python Senior?\n\ta)Леша\n\tб)Коля\n\tв)Андрей\n\tг)Петя")
a3=input('Ведите ответ:')
if a3==("г"):
    print('Правильно')
    answer=2.4+answer
else:
    print('Неправильно')
print("Ваш бал стал =",answer)
#4
print("4)В каком году хрестили русь?\n\ta)988\n\tб)998\n\tв)1000\n\tг)1002")
a4=input('Ведите ответ:')
if a4==("а"):
    print('Правильно')
    answer=2.4+answer
else:
    print('Неправильно')
print("Ваш бал стал =",answer)
#5
print("5)В какой галактике мы живем?\n\ta)млечный путь\n\tб)солнечная система\n\tв)вода\n\tг)земля")
a5=input('Ведите ответ:')
if a5==("а"):
    print('Правильно')
    answer=2.4+answer
else:
    print('Неправильно')
print("Ваш бал стал =",answer)
print('Твой бал состовляет =',answer)
input()