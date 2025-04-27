#countNumber using dict
def getUserNum():
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        
        # If the user enters a blank line, break out of the loop and stop asking for input
        if user_input == "":
            break
        
        # convert the user input to an integer and add it to the list
        num = int(user_input)
        user_numbers.append(num)
    return user_numbers
def countNum(lst):
    num_dict = {}
    for num in lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    return num_dict
def printCounts(num_dict):
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")
# user_numbers = getUserNum()
# num_dict = countNum(user_numbers)
# printCounts(num_dict)


#phonebook
def readphone():
    phonebook = {}                   # Create empty phonebook

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook

def printPhone(phonebook):
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))

def lookUpNumber(phonebook):
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])
# phonebook = readphone()
# printPhone(phonebook)
# lookUpNumber(phonebook)

def popUp():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input("How many (" + fruit_name + ") do you want to buy?: "))
        total_cost += (price * amount_bought)
    
    print("Your total is $" + str(total_cost))
popUp()