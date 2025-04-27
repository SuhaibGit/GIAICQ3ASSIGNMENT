import random
def guessNumber():
    secret_number = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99...")
    guess = int(input("Enter a guess: "))
    while guess != secret_number:
        if guess < secret_number:  
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        print() 
        guess = int(input("Enter a new guess: "))   
    print("Congrats! The number was: " + str(secret_number))
# guessNumber()

#fibonacci
def fibonacci():
    currTerm = 0 
    MAX_TERM_VALUE : int = 100
    nextTerm= 1
    while currTerm <= MAX_TERM_VALUE:
        print(currTerm)
        term_after_next = currTerm + nextTerm
        currTerm = nextTerm
        nextTerm = term_after_next
# fibonacci()

#to print 20 even numbers
def even():
    for i in range(20):
        print(i * 2)
# even()

#to validate user response

def wholeSome_Machine():
    AFFIRMATION : str = "Hello I am not a robot"
    print("Please type the following affirmation: " + AFFIRMATION)
    user_feedback = input()
    while user_feedback != AFFIRMATION:  
        print("That was not the affirmation.")
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()
    print("That's right! :)")
# wholeSome_Machine()
def liftoff():
    for i in range(10):
        print(10 - i)
    print("Liftoff!")
# liftoff()

def doubleIt():
    num:int=int(input("Enter number:2"))
    while(num<100):
        num=num*2
        print(str(num))
doubleIt()