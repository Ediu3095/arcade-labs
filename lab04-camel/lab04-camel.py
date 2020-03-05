import arcade
from random import randrange


def input_letter():
    run = True
    letter = ""
    while run:
        letter = input("What is your choice? ").upper()
        if letter in ["A", "B", "C", "D", "E", "Q"]:
            run = False
    return letter


def main():
    print("""Welcome to Camel!
    You have stolen a camel to make your way across the great Mobi desert.
    The natives want their camel back and are chasing you down! Survive your
    desert trek and out run the natives.\n""")

    done = False
    natives_traveled = -20
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    canteen_drinks = 3

    while not done:
        print("A. Drink from your canteen.\nB. Ahead moderate speed.\nC. Ahead full speed.\n"
              "D. Stop for the night.\nE. Status check.\nQ. Quit.\n")

        letter = input_letter()
        "The natives are getting close"
        if letter == "A":
            if canteen_drinks > 0:
                thirst = 0
                canteen_drinks -= 1
            else:
                print("Oh no!\nYou don't have water in the canteen!")
        elif letter == "B":
            miles_traveled += 5 + randrange(8)
            print("\nYou traveled %d miles\n" % miles_traveled)
            thirst += 1
            camel_tiredness += 1
            natives_traveled += 7 + randrange(8)
            oasis = randrange(20)
            if oasis == 10:
                print("You found an oasis!")
                canteen_drinks = 3
                thirst = 0
                camel_tiredness = 0
        elif letter == "C":
            miles_traveled += 10 + randrange(11)
            print("\nYou traveled %d miles\n" % miles_traveled)
            thirst += 1
            camel_tiredness += randrange(3) + 1
            natives_traveled += 7 + randrange(8)
            oasis = randrange(20)
            if oasis == 10:
                print("You found an oasis!")
                canteen_drinks = 3
                thirst = 0
                camel_tiredness = 0
        elif letter == "D":
            camel_tiredness = 0
            print("\nThe camel is happy to rest\n")
            natives_traveled += 7 + randrange(8)
        elif letter == "E":
            print("\nMiles traveled:  %d\nDrinks in canteen:  %d\nThe natives are %d miles behind you.\n"
                  % (miles_traveled, canteen_drinks, miles_traveled - natives_traveled))
        elif letter == "Q":
            print("Goodbye!")
            done = True

        if 4 < thirst < 6:
            print("You are thirsty")
        elif thirst > 6 and not done:
            print("You died of thirst!")
            done = True

        if 5 < camel_tiredness < 8:
            print("Your camel is tired")
        elif 8 < camel_tiredness and not done:
            print("Your camel is dead")
            done = True

        if miles_traveled - natives_traveled <= 0 and not done:
            print("The natives have caught you!")
            done = True
        elif 0 < miles_traveled - natives_traveled <= 15:
            print("The natives are getting close!")

        if miles_traveled >= 200 and not done:
            print("You made it across the desert! You won!")


main()
