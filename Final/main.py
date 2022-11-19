import random

from Person import Person

human = Person(name='Тарас', helth=100, mood=100, money=100)
human1 = Person(name='Коля', helth=100, mood=100, money=100)
human2 = Person(name='Петя', helth=100, mood=100, money=100)

while True:
    answer=0
    print(human)
    print()
    print(human1)
    print()
    print(human2)
    print()

    try:
        human.change_state(
            money=random.randint(50, 100),
            mood=random.randint(-20, -10),
            helth=random.randint(-10, -5)
        )
    except Exception:
        answer+=1
    try:
        human1.change_state(
            money=random.randint(50, 100),
            mood=random.randint(-20, -10),
            helth=random.randint(-10, -5)
        )
    except Exception:
        answer+=1
    try:
        human2.change_state(
            money=random.randint(50, 100),
            mood=random.randint(-20, -10),
            helth=random.randint(-10, -5)
        )
    except Exception:
        answer+=1
    if answer>2:
        break
print('------------------------------------------')
print(human)
print(human1)
print(human2)
# number=random.randint(1,3)
# if number==1:
#     human.work()
#     print('1')
# elif number==2:
#     human.rest()
#     print('2')
# elif number==3:
#     human.hospital()
#     print('3')
# else:
#     print('Error')
#
# print(human)
