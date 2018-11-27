# !/usr/bin/env python3

# Stwórz klasę dziedziczącą zmienne z klasy nadrzędnej
# Stwórz klasę dziedziczącą metody z klasy nadrzędnej
# Stwórz klasę która przeciąża metodę z klasy nadrzędnej i jednocześnie używa jej za pomocą słowa kluczowego super

class Vehicle(object):
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.wheels = 4

    def __del__(self):
        self.max_speed = None

    def go_back(self):
        print("I'm coming back! (Vehicle)")

class Car(Vehicle):
    def __init__(self, max_speed, doors):
        super(Car, self).__init__(max_speed)
        self.doors = doors

    def __del__(self):
        self.doors = None
        self.max_speed = None

    def vroom(self):
        print("Vroom vroom! (Car)")

class Audi(Car):
    def __init__(self, max_speed, doors, which_audi):
        super(Audi, self).__init__(max_speed, doors)
        self.which_audi = which_audi

    def __del__(self):
        self.max_speed = None
        self.doors = None
        self.which_audi = None

    def go_back(self):
        super(Audi, self).go_back()
        print("Beep beep. I have "+str(self.wheels)+" wheels! (Audi)")

    def get_into_my_audi(self):
        print("Now we're talking! (Audi)")


my_audi = Audi(180, 3, "A8")
my_audi.go_back()
my_audi.vroom()
my_audi.get_into_my_audi()
