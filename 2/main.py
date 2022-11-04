from Teacher import Teacher

from Student import Student

player1 = Teacher(name='Johan', damage=20)
player2 = Student(name='Mark', damage=5)
player3 = Student(name='Mike', damage=7)
player4 = Student(name='Maks', damage=9)

print(player1, '\n')
print(player2, '\n')
print(player3, '\n')
print(player4, '\n')

print('-----------Fight on Student-----------')
print('Attack Mark')
player1.attack(player2)
print(player2, '\n')
print('Attack Mike')
player1.attack(player3)
print(player3, '\n')
print('Attack Maks')
player1.attack(player4)
print(player4, '\n')
print('-----------Fight on Teacher-----------')

player2.attack(player1)
print(player1, '\n')
player3.attack(player1)
print(player1, '\n')
player4.attack(player1)
print(player1, '\n')
print('---------------Finish-----------------')
print(player1, '\n')
print(player2, '\n')
print(player3, '\n')
print(player4, '\n')

while True:
    input()
