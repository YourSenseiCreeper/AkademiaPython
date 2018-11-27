# !/usr/bin/env python3

# Pobierz od użytkownika jego imię, nazwisko i wiek, wyświetl je na ekranie.
# Stwórz funkcje, które pobierze od użytkownika liczbę, dokona jej konwersji na odpowiedni typ i wyświetl tę liczbę.
# Stwórz prostą klasę, która przyjmie jako parametry dane pobrane od użytkownika. Niech klasa ta opisuje kwiata.

def get_age():
    age = input("Ile w ogóle masz lat?\n")
    age = int(age)
    print("Masz {} lat!".format(age))
    return age


name = input("Jak masz na imię?\n")
surname = input("Jakie masz nazwisko?\n")
your_age = get_age()

print("Cześć! Nazywasz się {} {} i masz {} lat!".format(name, surname, your_age))

class Flower(object):
    def __init__(self, flower_name, color, when_grows):
        self.flower_name = flower_name
        self.color = color
        self.when_grows = when_grows

    def __del__(self):
        self.flower_name = None
        self.color = None
        self.when_grows = None

    def describe(self):
        print("{} jest {} i kwitnie {}".format(self.flower_name, self.color, self.when_grows))


flower_name = input("Jak nazywa się twój kwiatek?\n")
color = input("Jakiego jest koloru?\n")
when_grows = input("Kiedy kwitnie?\n")

my_flower = Flower(flower_name, color, when_grows)
my_flower.describe()
