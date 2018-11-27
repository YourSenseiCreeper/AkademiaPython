# !/usr/bin/env python3
class Food(object):

    def __init__(self, liquid, weight, volume):
        self.liquid = liquid
        self.weight = weight
        self.volume = volume
        print("That's the Food class!")

    def __del__(self):
        self.liquid = None
        self.weight = None
        self.volume = None
        print("All variables died (Food)!")

    def is_liquid(self):
        return self.liquid

    def get_dencity(self):
        return self.weight/self.volume

class Pizza(Food):
    def __init__(self, acridiness, size):
        self.acridiness = acridiness
        self.size = size
        print("That's the Pizza class!")

    def __del__(self):
        self.acridiness = None
        self.size = None
        print("All variables died! (Pizza)")

    def serve_pizza(self):
        print("Here you are! That's "+self.size+" pizza!")

    def refound_pizza(self):
        print("I want a refound! This pizza is cold as an iceberg!")

class ChocolateBar(Food):
    def __init__(self, caloricityA, cocoaBeanContentA):
        self.caloricity = caloricityA
        self.cocoaBeanContent = cocoaBeanContentA
        print("That's the ChocolateBar class!")

    def __del__(self):
        self.caloricity = None
        self.cocoaBeanContent = None
        print("All variables died! (ChocolateBar)")

    def get_caloricity(self):
        return self.caloricity

    def get_cocoa_beans_content(self):
        return self.cocoaBeanContent


my_bar = ChocolateBar(1000, 0.70)
my_food = Food(False, 2.25, 0.05)
my_pizza = Pizza("Mild", "Medium")
my_pizza.serve_pizza()
