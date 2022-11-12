from Teacher import Teacher
import random


class Samurai(Teacher):
    max_health = 200
    combo = 0
    max_combo = 5
    def __init__(self, name='', helth=200, damage=1, defense=0):
        Teacher.__init__(self, name, helth, damage, defense)
        self.max_health = self.helth
    def attack(self, target: Teacher):
        if self.combo > 5:
            target.take_damage(self.damage)
            self.combo += 1
        else:
            target.take_damage(self.damage + self.damage * 0.1)
            self.combo += 1
1
