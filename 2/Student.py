class Student:
    name = ''
    helth = 100
    damage = 1
    defense = 0

    def __init__(self, name='', helth=100, damage=1, defense=0):
        self.name = name
        self.helth = helth
        self.damage = damage
        self.defense = defense

    def __str__(self):
        return f' == {self.name} ==\n' \
               f'Health: {self.helth}\n' \
               f'Damage: {self.damage}\n' \
               f'Defense: {self.defense}'

    def take_damage(self, damage=0):
        self.helth -= max(damage, 0)

    def attack(self, target ):
        target.take_damage(self.damage)