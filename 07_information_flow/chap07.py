#choosing return
ADULT_AGE : int = 18 # U.S. age 

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    else:
        return False
# age : str = int(input("How old is this person?: "))
# print(is_adult(age))


#greeting
def greet(name):
    return "Greetings " + name + "!"
# name : str = input("What's your name? ")
# print(greet(name))

def in_range(n, low, high):
    if n >= low and n <= high:
        return True
    return False   
# in_range(6,5,9)


#instock
def num_in_stock(fruit):
	if fruit == 'apple':
		return 2
	if fruit == 'durian':
		return 4
	if fruit == 'pear':
		return 1000
	else:
		# this fruit is not in stock.
		return 0
# fruit : str = input("Enter a fruit: ")
# stock = num_in_stock(fruit)
# if stock == 0:
#     print("This fruit is not in stock.")
# else:
#     print("This fruit is in stock! Here is how many:")
#     print(stock)


#user info
def get_user_info():
    first_name: str = input("What is your first name?: ")
    last_name: str = input("What is your last name?: ")
    email_address : str = input("What is your email address?: ")
    
    return first_name, last_name, email_address
# user_data = get_user_info()
# print("Received the following user data:", user_data)

#subtract 7
def subtract_seven(num):
	num = num - 7
	return num
num: int = 7
num = subtract_seven(num)
print("this should be zero: ", num)