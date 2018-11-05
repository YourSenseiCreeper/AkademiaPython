class Food(object):

    def __init__(self, liquid, weight, volume):
        self.liquid = liquid
        self.weight = weight
        self.volume = volume
        print("That's the Food class!")

    def __del__(self):
        self.liquid
        self.weight
        self.volume
        print("All variables died (Food)!")

    def isLiquid(self):
        return self.liquid

    def getDencity(self):
        return self.weight/self.volume

class Pizza(Food):
    def __init__(self, acridiness, size):
        self.acridiness = acridiness
        self.size = size
        print("That's the Pizza class!")

    def __del__(self):
        self.acridiness
        self.size
        print("All variables died! (Pizza)")

    def servePizza(self):
        print("Here you are! That's "+self.size+" pizza!")

    def refoundPizza(self):
        print("I want a refound! This pizza is cold as the iceberg!")

class ChocolateBar(Food):
    def __init__(self, caloricityA, cocoaBeanContentA):
        self.caloricity = caloricityA
        self.cocoaBeanContent = cocoaBeanContentA
        print("That's the ChocolateBar class!")

    def __del__(self):
        self.caloricity
        self.cocoaBeanContent
        print("All variables died! (ChocolateBar)")

    def getCaloricity(self):
        return self.caloricity

    def getCocoaBeanContent(self):
        return self.cocoaBeanContent


my_bar = ChocolateBar(1000, 0.70)
my_food = Food(False, 2.25, 0.05)
my_pizza = Pizza("Mild", "Medium")