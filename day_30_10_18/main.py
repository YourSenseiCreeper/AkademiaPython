# class Neighbourhood():
#     pass
#
# def create_neighbourhood():
#     return Neighbourhood()
#
#
# labels = ["Pierwszy", "Drugi", "Trzeci", "Czwarty", "Kolejny"]
#
# def lista(*zawodnicy):
#     for i in range(0, len(zawodnicy)):
#         if i < 4:
#             print(labels[i] + ": " + zawodnicy[i])
#         else:
#             print(labels[-1] + ": " + zawodnicy[i])
#
#
# my_new_neighbour = create_neighbourhood()
# print(my_new_neighbour)
#
# lista("Adam", "Lukasz", "Marek", "Tomek", "Mariusz", "Barnaba", "Seba")
#
# class LivingCreature(object):
#     def WhatRUDoing(self):
#         return "Living!"
#
# class Dog(LivingCreature):
#     def HowHow(self):
#         print("How how!")
#
# class Sunflower(LivingCreature):
#     def SunGoesDown(self):
#         print("Goodbye!")
#
# sunflower = Sunflower()
# dog = Dog()
#
# print("Dog: "+dog.WhatRUDoing())
# print("Sunflower: "+sunflower.SunGoesDown())
import random

class Human(object):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        print("Moje imie to %s" %name)
        print("A nazwisko to %s" %surname)

piotrek = Human("Piotr", "Wereszczynski")

def randomNumbers():
    for i in range(1, 10):
        yield random.randint(1, 10)

print(list(randomNumbers()))

fibolist = [1, 1]
def fibo(n):
    for i in range(n):
        fibolist.append((fibolist[-2]+fibolist[-1]))


fibo(12)
print(fibolist)
# Zad dom - własna klasa + constructor + destructor + jakieś metody +
# Rozszerzenie tej klasy o jakieś wartości w nowej klasie