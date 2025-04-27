#average of 2 number
def average(a:float,b:float):
    sum = a + b
    return sum / 2
# print("Average of 2 numbers are:",average(5,6))


#chaotic counting
# def counting():
#     for i in range(10):
#         curr_num = i + 1
#         if done():
#             return # this ends the function execution, so we'll get back to the main() function!
#         print(curr_num)
# def done():
#     """ Returns True with a probability of DONE_LIKELIHOOD """
#     if random.random() < DONE_LIKELIHOOD:
#         return True
#     return False

# print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
# counting()
# print("I'm done")


 #count even
def countEven():
    count = 0  
    for num in lst:  
        if num % 2 == 0:  
            count += 1
    print(count)

def get_list_of_ints():
    lst = []  
    user_input = input("Enter an integer or press enter to stop: ")  
    while user_input != "":  
        lst.append(int(user_input)) 
        user_input = input("Enter an integer or press enter to stop: ")  

    return lst

# lst = get_list_of_ints()
# countEven(lst)

#douvble
def double(num: int):
    return num * 2
# num = int(input("Enter a number: "))
# num_times_2 = double(num)
# print("Double that is", num_times_2)

#getname
def getName():
    return "Sophia"
# name = getName() # get_name() will return a string which we store to the 'name' variable here
# print("Howdy", name, "! <:")


#is_odd 
def is_odd(value: int):
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1
# for i in range(10):
#         if is_odd(i):
#             print('odd')
#         else:
#             print('even')

#divisor
def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)
# num = int(input("Enter a number: "))
# print_divisors(num)

#print multiple



