import random
randnumber = random.randint(1, 100)
userguess = None
guesses = 0
print(randnumber)

while (userguess != randnumber):
    userguess = int(input("Enter your Number: "))
    guesses = 1 + guesses
    if userguess == randnumber:
        print("you guess the right number")
    else:
        print("you enter wrong number")


