# !/usr/bin/env python3

import math

test_nbr = 0
# ● Napisz funkcję, która pobierze od użytkownika imię i sprawdzi czy jest takie
# samo jak twoje. W przypadku gdy jest równoważne wyświetli inne powitanie
# niż w sytuacji gdy to imię jest inne.

name = input("Podaj swoje imię:\n")
if name in ("Piotr", "Piotrek", "Piter"):
    print(test_nbr, "Witaj Pitercjuszu! Dobrze Cię widzieć!\n")
else:
    print(test_nbr, "Cześć", name)
test_nbr += 1

# ● Napisz funkcję, która pobierze od użytkownika liczbę i gdy jest to liczba
# różna różna od zera wyświetli ją. Gdy jest to zero wyświetli napis dowolny
# napis. Do sprawdzenia wartości nie używa operatorów porównania.

number = input("Podaj mi jakąś liczbę całkowitą:\n")
number = int(number)
if number is 0:
    print(test_nbr, "Mniej niż zeroooooo!")
else:
    print(test_nbr, "Twoja liczba to:", number)
test_nbr += 1

# ● Napisz klasę dla dowolnej bryły, która będzie posiadała wszystkie funkcje
# pozwalające porównywać obiekty tej klasy.

class Cone(object):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.volume = 1/3*(math.pi*radius**2)*height

    def __eq__(self, other):
        return self.height is other.height and self.radius is other.radius

    def eq_volume(self, other):
        return self.volue == other.volue

    def eq_radius(self, other):
        return self.radius == other.radius

    def eq_height(self, other):
        return self.height == other.height


cone_1 = Cone(5, 15)
cone_2 = Cone(5, 2)

if cone_1 != cone_2:
    print(test_nbr, "Cone test passed!")
test_nbr += 1

# ● Napisz klasę dla dowolnej figury płaskiej, która będzie posiadała wszystkie
# funkcje pozwalające porównywać obiekty tej klasy.

class Trapeze(object):
    def __init__(self, base_a, base_b, height):
        self.base_a = base_a
        self.base_b = base_b
        self.height = height
        self.area = (base_a + base_b) * height / 2

    def __eq__(self, other):
        return self.base_a is other.base_a and self.base_b is other.base_b and self.height is other.height


trapeze_1 = Trapeze(5, 10, 15)
trapeze_2 = Trapeze(5, 10, 15)

if trapeze_1 == trapeze_2:
    print(test_nbr, "Trapeze test passed!")
test_nbr += 1

# ● Stwórz drzewo klas (min. 6 klas, min. 2 poziomy dziedziczenia), w którym
# każda klasa posiada komplet funkcji pozwalających porównywać obiekty tej
# klasy. Nie może to być drzewo brył ani drzewo figur płaskich.

class Weapon(object):
    def __init__(self, damage=0, reload_time=0):
        self.damage = damage
        self.reload_time = reload_time

    def __eq__(self, other):
        return self.damage is other.damage and self.reload_time is other.reload_time

class WhiteWeapon(Weapon):
    def __init__(self, damage, reload_time, range_type="low range"):
        super(WhiteWeapon, self).__init__(damage, reload_time)
        self.range_type = range_type

    def __eq__(self, other):
        return super(WhiteWeapon, self) is super(WhiteWeapon, other) and \
               self.range_type is other.range_type

class Knife(WhiteWeapon):
    def __init__(self, length, grip_type, damage, reload_time, range_type="low range"):
        super(Knife, self).__init__(damage, reload_time, range_type)
        self.length = length
        self.grip_type = grip_type

    def __eq__(self, other):
        return super(Knife, self) is super(Knife, other) and \
               self.length is other.length and self.grip_type is other.grip_type
class Gun(Weapon):
    def __init__(self, calibre, weigth, magazine_size, damage, reload_time):
        super(Gun, self).__init__(damage, reload_time)
        self.calibre = calibre
        self.weigth = weigth
        self.magazine_size = magazine_size

    def __eq__(self, other):
        return super(Gun, self) is super(Gun, other) and \
               self.calibre is other.calibre and self.weigth is other.weigth and \
               self.magazine_size is other.magazine_size

class Glock(Gun):
    def __init__(self, model, calibre, weight, magazine_size, damage, reload_time):
        super(Glock, self).__init__(calibre, weight, magazine_size, damage, reload_time)
        self.model = model

    def __eq__(self, other):
        return super(Glock, self) is super(Glock, other) and \
               self.calibre is other.calibre

class Mp40(Gun):
    def __init__(self, fire_modes, model, calibre, weight, magazine_size, damage, reload_time):
        super(Mp40, self).__init__(calibre, weight, magazine_size, damage, reload_time)
        self.model = model
        self.fire_modes = fire_modes

    def __eq__(self, other):
        return super(Mp40, self) is super(Mp40, other) and \
               self.model is other.model and self.fire_modes == other.fire_modes


my_weapon_1 = Weapon(1, 1)
my_weapon_2 = Weapon(1, 2)

my_wweapon_1 = WhiteWeapon(5, 0, "very low range")
my_wweapon_2 = WhiteWeapon(7, 3, "long range")

my_knife_1 = Knife(10, "Warrior", 5, 0, "very low range")
my_knife_2 = Knife(11, "Anaconda", 9, 0, "very low range")

my_gun_1 = Gun(6.95, 1.15, 10, 55, 3)
my_gun_2 = Gun(7.55, 1.5, 10, 80, 4)

my_glock_1 = Glock(11.5, 6.67, 2.1, 12, 88, 3)
my_glock_2 = Glock(12.5, 7.15, 2, 14, 90, 4)

my_mp40_1 = Mp40(["Auto", "OneShot"], 1.0, 6.67, 3.5, 100, 120, 5)
my_mp40_2 = Mp40(["Auto", "Semi-Auto"], 1.1, 6.34, 3.25, 110, 125, 6)

if my_weapon_1 != my_weapon_2:
    print(test_nbr, "Weapon test passed!")
    test_nbr += 1
if my_wweapon_1 != my_wweapon_2:
    print(test_nbr, "WhiteWeapon test passed!")
    test_nbr += 1
if my_knife_1 != my_knife_2:
    print(test_nbr, "Knife test passed!")
    test_nbr += 1
if my_gun_1 != my_gun_2:
    print(test_nbr, "Gun test passed!")
    test_nbr += 1
if my_glock_1 != my_glock_2:
    print(test_nbr, "Glock test passed!")
    test_nbr += 1
if my_mp40_1 != my_mp40_2:
    print(test_nbr, "Mp40 test passed!")
