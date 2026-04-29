import random

from matplotlib.pylab import roll

class player:
    def __init__(self, name, money):
        self.name= name
        self.money= money
        self. position= 0
        self.properties= []

    def move(self, steps):
        self.position += steps
        print(f"{self.name} move {steps} steps to position {self.position}")

    def pay(self, amount):
        self.money -= amount
        print(f"{self.name} pay {amount}. remaining {self.money}")

    def receive(self, amount):
        self.money += amount
        print(f"{self.name} receive {amount}. total {self.money}")

    def dice(self):
        print (f"{self.name} rolls the dice...")
        roll = random.randint(1, 6)
        print (f"{self.name} rolled: {roll}")
        return roll        