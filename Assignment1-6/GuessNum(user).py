import random
def computerGuess(x):
    low=1
    high=x
    feedback=''
    while feedback!="c":
        if low!=high:
            guess= random.randint(low,high)
        else:
            guess=low
        feedback=input(f'Is {guess} is too high(H), too low(L), correct(C)??:').lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f"Congratulation! your computer guess your number {guess} correct")
computerGuess(10)