class Bad(Exception):
    def __init__(self, message):
        Exception.__init__(message)


class Person:
    name = ''
    helth = 100
    mood = 100
    money = 100

    def __init__(self, name='', helth=100, mood=100, money=100):
        self.name = name
        self.helth = helth
        self.mood = mood
        self.money = money

    def __str__(self):
        return f' == {self.name} ==\n' \
               f'Health: {self.helth}\n' \
               f'Mood: {self.mood}\n' \
               f'Money: {self.money}'

    def change_state(self, money, mood, helth):
        self.helth += helth
        self.mood += mood
        self.money += money
        if self.helth < 0:
            raise Exception('Голод')
        if self.mood < 0:
            raise Exception('Депресия')
        if self.money < 0:
            raise Exception('Банкротство')
        if helth > 200:
            self.helth = 15
        if mood > 200:
            self.helth = 15



    # go_to_factory = Work(name='Пойти на завод', money=50, mood=-10, health=-3)
    # go_to_park = Rest(name='Сходить в парк', money=0, mood=15, health=3)
    # go_to_hospital = Action(name='Пойти в больницу', money=-20, mood=-5, health=20)
    def work(self, money=50, mood=-10, helth=-3):
        self.helth += helth
        self.mood += mood
        self.money += money

    def rest(self, money=0, mood=15, helth=3):
        self.helth += helth
        self.mood += mood
        self.money += money

    def hospital(self, money=-50, mood=-5, helth=20):
        self.helth += helth
        self.mood += mood
        self.money += money
