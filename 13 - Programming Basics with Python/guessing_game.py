import random


def guessingNumberGame(minNumber, maxNumber):
    targetNumber = random.randint(minNumber, maxNumber)

    guesseNumber = 0
    attempNumber = 0

    while guesseNumber != targetNumber:
        try:
            guesseNumber = int(input(f"Enter The Guess Number Between {minNumber} and {maxNumber} \n : "))
        except:
            print("Enter valid number")

        attempNumber = attempNumber + 1


        print(f"Attemp  {attempNumber}")
        if guesseNumber == targetNumber :
            print(f"Congratulations! 🎉🎉 You Guess the correct Number")
        elif guesseNumber < targetNumber :
            print("Your Number Is Low! Try Again")
        else:
            print("Your Number Is High! Try Again")
    

guessingNumberGame(10, 200)