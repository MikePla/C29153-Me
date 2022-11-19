import random
from Person import Person

human = Person(name='Тарас', helth=100, mood=100, money=100)
number=random.randint(1,3)
if number==1:
    human.work()
    print('1')
elif number==2:
    human.rest()
    print('2')
elif number==3:
    human.hospital()
    print('3')
else:
    print('Error')

print(human)