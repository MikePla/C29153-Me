from Teacher import Teacher

player1 = Teacher(name='Johan', damage=12)
player2 = Teacher(name='Mark', damage=11)

print(player1, '\n')
print(player2, '\n')
print('--------------Fight--------------')

while player1.is_alive() and player2.is_alive():
    player1.attack(player2)
    player2.attack(player1)

    print(player2, '\n')
    print(player1, '\n')
'''
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
'''

while True:
    input()
