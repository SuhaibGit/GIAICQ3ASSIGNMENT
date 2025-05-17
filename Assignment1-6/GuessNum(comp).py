import random
def guess(x):
    randomNumber=random.randint(1,x)
    guess = 0
    while (guess!=randomNumber):
        guess=int(input(f"guess the numebr between 1 and {x}: "))
        if guess<randomNumber:
            print("Your guess is low, guess again")
        elif guess>randomNumber:
            print("Your guess is high guess again")

    print("Congratulation!  you guess the right one")
guess(10)