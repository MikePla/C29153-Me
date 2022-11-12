from berserk import Berserk
from Teacher import Teacher
from assasin import Assasin
from samurai import Samurai


#player1 = Berserk(name='Berserk', damage=25 ,helth=1500)
#player2 = Teacher(name='Teacher', damage=17)
player3 = Assasin(name='Assasin', damage=12)
player4 = Samurai(name='Samurai', damage=14)


#print(player1, '\n')
#print(player2, '\n')
print(player3, '\n')
print(player4, '\n')

print('============================================================================= \n')
while player3.is_alive() and player4.is_alive() :
    player3.attack(player4)
    player4.attack(player3)

    print(player3, '\n')
    print(player4, '\n')
