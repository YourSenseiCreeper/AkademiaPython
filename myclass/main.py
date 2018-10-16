# greetings = str("lol")
# print(greetings)
#
# def loadAllData():
#     greetings = "Nie wiem co"
#     print(greetings)
#     return;
#
# loadAllData()
#
# fruit = "bananas"
# basket = {"banana", "grape", "pineapple"}
# print(fruit in basket)
#
# basket.append("lemon")
#
# print(basket)
#
# height = 1.78
# print("Moj wzrost to ",height,"m")
#
# nameAndSurname = "Piotr Wereszczyński"
# print(nameAndSurname)
#
# age = 19
# print("Mam ",age," lat")

class MyName:
    imie = "Piotr"
    nazwisko = "Wereszczynski"

this_is_myName = MyName()
print(this_is_myName.imie, this_is_myName.nazwisko)

this_is_myName.imie = "Damian"
print(this_is_myName.imie, this_is_myName.nazwisko)