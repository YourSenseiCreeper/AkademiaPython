import winsound

# The Definition of domain - C major scale
# 0 for no sound
signToNumber = input("Podaj znak: ")
print(ord(signToNumber))

scale = ['0', 'C', 'D', 'E', 'F', 'G', 'A', 'H']
noteAssignment = {
        "C": "/files/sounds/NoteC(2).wav",
        "D": "/files/sounds/NoteD(2).wav",
        "E": "/files/sounds/NoteE(2).wav",
        "F": "/files/sounds/NoteF.wav",
        "G": "/files/sounds/NoteG.wav",
        "A": "/files/sounds/NoteA.wav",
        "H": "/files/sounds/NoteH.wav",
        "0": "/files/sounds/NoteNull.wav"
        }

def ConvertToNotes(number):
    result = ""
    while number > 0:
        result += scale[int((number % 8))]
        number = (number - (number % 8)) / 8
    return result[::-1]

def ConvertToNumber(notes):
    reversed_notes = notes[::-1]
    result = 0
    exponent = 0
    for sign in reversed_notes:
        result += scale.index(sign)*(8**exponent)
        exponent += 1
    return result


word = input("Podaj słowo do przekonwertowania na dzwięk: ")
for letter in word:
    print(letter, ord(letter))
    scaleResult = ConvertToNotes(ord(letter))
    for sign in scaleResult:
        print(sign)
        winsound.PlaySound(noteAssignment.get(sign, "C"), winsound.SND_FILENAME)
        winsound.PlaySound()
        
# for x in range(10):
#     number = int(input("Podaj liczbe do przekonwertowania na dzwiek: "))
#     print("Number: %d", number)
#
#     scaleResult = ConvertToNotes(number)
#     for sign in scaleResult:
#         print(sign)
#         winsound.PlaySound(noteAssignment.get(sign, "C"), winsound.SND_FILENAME)

# for x in range(10):
#     chain = input("Podaj nuty do przekonwertowania na liczbę: ")
#     print("Twoja liczba to: ", ConvertToNumber(chain))
