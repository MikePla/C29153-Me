import datetime


class Student:
    name = ''
    helth = 100
    damage = 1
    defense = 0
    old = 2008
    group = 'C29153'

    def __init__(self, name='', helth=100, damage=1, defense=0, group='C29153', old=2008):
        self.name = name
        self.helth = helth
        self.damage = damage
        self.defense = defense
        self.group = group
        self.old = old

    def get_age(self,):
        return datetime.date.today().year - self.old

    def __str__(self):
        return f' == {self.name} ==\n' \
               f'Health: {self.helth}\n' \
               f'Damage: {self.damage}\n' \
               f'Defense: {self.defense}\n' \
               f'Old: {self.get_age()}\n' \
               f'Froup: {self.group}'

    def take_damage(self, damage=0):
        self.helth -= max(damage, 0)

    def attack(self, target):
        target.take_damage(self.damage)
    def is_alive(self):
        if self.helth <= 0:
            return False
        else:
            return True
