from random import randint
class Cat():
    def __init__(self, name):
        self.name = name
        self.power = 50
        self.age = 0
        self. house = None
    def go_into_house(self,house):
        self.house = house
        self.power -= 30
    def play(self):
        print(f"{self.name} play a ball")
        self.power -= 10
    def eat(self):
        print(f"{self.name} eat a meal")
        self.power += 20
        self.house.food -= 10
    def sleep(self):
        print(f"{self.name} sleep all night")
        self.power += 50
        self.age += 1
    def walk(self):
        print(f"{self.name} walk down the street")
        self.power -= 15
    def __str__(self):
        return f"i'm cat, my name is: {self.name},i live in house: {self.house}, my life force is: {self.power}, my age is: {self.age} days"

class House():
    def __init__(self, name):
        self.name = name
        self.food = 100

    def __str__(self):
        return f"house name is: {self.name}"

my_house = House
barsik = Cat("Barsik")
barsik.go_into_house("my_house")
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
