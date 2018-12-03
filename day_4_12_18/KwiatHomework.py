# !/usr/bin/env python3

# Pobierz od użytkownika jego imię, nazwisko i wiek, wyświetl je na ekranie.

# Stwórz funkcje, które pobierze od użytkownika liczbę,
# dokona jej konwersji na odpowiedni typ i wyświetl tę liczbę.

# Stwórz prostą klasę, która przyjmie jako parametry dane
# pobrane od użytkownika. Niech klasa ta opisuje kwiata.

name = input("Podaj swoje imię:\n")
surname = input("Podaj swoje nazwisko:\n")
age = input("Ile masz lat?\n")

print("Nazywasz się", name, surname, "i masz", age, "lat!\n")

def get_number():
    user_number = input("Podaj liczbę:\n")
    user_number = float(user_number)
    if (user_number - (user_number // 1)) == 0:
        user_number = int(user_number)
    print("Twoja liczba to:", user_number, "jest typu", type(user_number))

class MyLittleFlower(object):
    def __init__(self, colour, smell, flower_name):
        self.colour = colour
        self.smell = smell
        self.flower_name = flower_name

    def __del__(self):
        self.colour = None
        self.smell = None
        self.flower_name = None

    def describe(self):
        print("Your", self.flower_name, "is", self.colour, "and smells", self.smell)


get_number()
my_flower = MyLittleFlower("black", "lovely", "black rose")
my_flower.describe()