import random
print("Welcome to your Password Generator")
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?1234567890'
numbers=int(input('Enter the Amount of password to generate:'))
length=int(input('Input your password length:  '))
print('\nHere are your passwords: ')
for pwd in range(numbers):
    passwords=''
    for c in range(length):
        passwords+=random.choice(chars)
    print(passwords)

