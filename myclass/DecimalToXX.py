signTable = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N' 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'W']

XXXXsignTable = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'w', '@', '!', '$', '&', '/', '%', '^', '#',
                 '?', '*', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S',
                 'T', 'X', 'Y', 'Z']

print(len(signTable))

def DecimalToXX(number):
    result = ""
    while number > 0:
        result += signTable[int((number % 32))]
        number = (number - (number % 32)) / 32
    return result[::-1]

def DecimalToXXXX(number):
    result = ""
    while number > 0:
        result += XXXXsignTable[int((number % 64))]
        number = (number - (number % 64)) / 64
    return result[::-1]

number = int(input("Podaj liczbę do przekonwertowania: "))
print("W XX to jest: ", DecimalToXX(number))
print("W XXXX to jest: ", DecimalToXXXX(number))
print("W X to jest: ", hex(number))
print("W Oct to jest: ", oct(number))
print("W Bin to jest: ", bin(number))