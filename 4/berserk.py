from Teacher import Teacher


class Berserk(Teacher):
    max_health = 200

    def __init__(self, name='', helth=200, damage=1, defense=0):
        Teacher.__init__(self, name, helth, damage, defense)
        self.max_health = self.helth

    def count_additional_damage(self):
        return self.damage * (1 - self.helth / self.max_health)

    def attack(self, target: Teacher):
        target.take_damage(self.damage + self.count_additional_damage())
