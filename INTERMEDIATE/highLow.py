import random
rounds=3
def HighLow():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    score=0
    for i in range(rounds):
        print("Round", i + 1)
        value = random.randint(1, 100)
        compValue = random.randint(1, 100)
        print("Your number is", value)
        choice: str = input("Do you think your number is higher or lower than the computer's?: ")
        higher:bool = choice=="higher" and value > compValue
        lower:bool = choice=="lower" and value< compValue
        if higher or lower:
            print("You were right! The computer's number was", compValue)
            score+=1
        else:
            print("Aww, that's incorrect. The computer's number was", compValue)
        print("Your score is now", score)
        print()
    print("Thanks for playing!")
HighLow()