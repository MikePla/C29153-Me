class Action:
    name='Hospital'
    helth = 20
    mood = -5
    money = -20
    def __init__(self, name='', helth=0, mood=0, money=0):
        self.name = name
        self.helth = helth
        self.mood = mood
        self.money = money