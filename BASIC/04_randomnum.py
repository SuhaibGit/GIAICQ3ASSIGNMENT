import random
def printRandom():
    N_NUMBERS: int = 10
    MIN_VALUE: int = 1
    MAX_VALUE: int = 100
    for i in range(0,N_NUMBERS):
        value = random.randint(MIN_VALUE, MAX_VALUE)
        print(value)
printRandom()