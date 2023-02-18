class Cat():
    def __init__(self, name):
        self.name = name
        self.power = 50
        self.age = 0
    def play(self):
        self.power -= 10
    def eat(self):
        self.power += 20
    def sleep(self):
        self.power += 50
        self.age += 1
    def __str__(self):
        return f"i'm cat, my name is: {self.name}, my life force is: {self.power}, my age is: {self.age} days"
