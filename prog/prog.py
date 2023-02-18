from random import randint
class Cat():
    def __init__(self, name):
        self.name = name
        self.power = 50
        self.age = 0
    def play(self):
        print(f"{self.name} play a ball")
        self.power -= 10
    def eat(self):
        print(f"{self.name} eat a meal")
        self.power += 20
    def sleep(self):
        print(f"{self.name} sleep all night")
        self.power += 50
        self.age += 1
    def walk(self):
        print(f"{self.name} walk down the street")
        self.power -= 15
    def __str__(self):
        return f"i'm cat, my name is: {self.name}, my life force is: {self.power}, my age is: {self.age} days"

barsik = Cat("Barsik")
for day in range(7):
    print(f"======================= {day} =========================")
    cube = randint(1, 6)
    if cube == 1 or 3 :
        barsik.play()
    elif cube == 2 or 4 :
        barsik.walk()
    else:
        barsik.eat()
    barsik.sleep()
    print(barsik)
