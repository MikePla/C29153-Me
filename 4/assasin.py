from Teacher import Teacher
import random


class Assasin(Teacher):
    max_health = 200
    combo = 0

    def __init__(self, name='', helth=200, damage=1, defense=0):
        Teacher.__init__(self, name, helth, damage, defense)
        self.max_health = self.helth

    def attack(self, target: Teacher):
        krit = random.randint(1, 5)
#шанс 20%
        if krit == 6:
            target.take_damage(1000)
            self.helth += self.damage * 0.1
            print(f'===krit===\n')

        else:
            target.take_damage(self.damage)
        #   def take_damage(self, damage=0):
        #   ninnja = random.randint(1, 10)
        # self.helth -= max(damage, 0)
        ##    self.helth = max(self.helth - max(damage, 0),0)

        #  if self.combo > 5:
        #      target.take_damage(self.damage)
        #     self.combo += 1
        # target.take_damage(self.damage + self.damage * 0.1)
# типа обычный урон его 14 а урон 1000=986(крит урон)+14
#
# def attack(self, target: Teacher):
#     target.take_damage(self.damage)
