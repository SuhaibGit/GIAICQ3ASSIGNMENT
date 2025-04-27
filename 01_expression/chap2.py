import random
import math
NUM_SIDES = 6

def roll_dice():
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print("Total of two dice:", total)


# die1: int = 10
# print("die1 in main() starts as: " + str(die1))
# roll_dice()
# roll_dice()
# roll_dice()
# print("die1 in main() is: " + str(die1))


#mass energy
def massEnergy():
    mass:float = float(input("Enter mass in KG: "))
    c:float = 29979458
    energy: float = mass * (c ** 2)
    print("e = m * C^2...")
    print("m = " + str(mass) + " kg")
    print("C = " + str(c) + " m/s")
    
    print(str(energy) + " joules of energy!")
# massEnergy()


#inches to foot
def convInch_Foot():
    value:int=12
    feet:float=float(input("Enter number of feet: "))
    inches:float=feet*value
    print("That is",str(inches),"in inches")
# convInch_Foot()

#pythagorain theorem
def theorem():
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))
    bc: float = math.sqrt(ab**2 + ac**2)
    print("The length of BC (the hypotenuse) is: " + str(bc))
# theorem()

#remainder division
def reamainderDevision():
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))
    quotient: int = dividend // divisor  
    remainder: int = dividend % divisor  
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))
# reamainderDevision()


#roll dice
def rollDice2():
    NUM_SIDES: int = 6
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)
# rollDice2()

#second in year
def SecInYear():
    DAYS_PER_YEAR: int = 365
    HOURS_PER_DAY: int = 24
    MIN_PER_HOUR: int = 60
    SEC_PER_MIN: int = 60
    print("There are " + str(DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN) + " seconds in a year!")
# SecInYear()

def tiny_mad_lib():
    SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my "
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    # Join the inputs together with the sentence starter
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")
tiny_mad_lib()