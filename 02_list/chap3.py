#addition of number given in list
def addManyNum(numbers)->int:
      # Make a list of numbers
    total_so_far: int = 0
    for number in numbers:
        total_so_far += number
    return total_so_far
# numbers: list[int] = [1, 2, 3, 4, 5]
# sum_of_numbers: int = addManyNum(numbers)
# print(sum_of_numbers)  

#double list
def doubleList():
    numbers: list[int] = [1, 2, 3, 4]  # Creates a list of numbers

    for i in range(len(numbers)):  # Loop through the indices of the list
        elem_at_index = numbers[i]  # Get the element at index i in the numbers list
        numbers[i] = elem_at_index * 2  # Set the element at index i to be equal to the previous element times 2

    print(numbers)  # This should print the doubled list
# doubleList()

#data structure
def dataStructure(my_list,data):
    for i in range(3):
        my_list.append(data)
# message = input("Enter a message to copy: ")
# my_list = []
# print("List before:", my_list)
# dataStructure(my_list, message)
# print("List after:", my_list)


#getlist
def get_first_element(lst):
    print(lst[0])

def get_last_Element(lst):
    print(lst[-1])

def get_whole_list(lst):
    print("Here's the list:", lst)

MAX_LENGTH : int = 3
def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)


def getlist():
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst
# lst = getlist()
# get_first_element(lst)
# get_last_Element(lst)
# get_whole_list(lst)
# shorten(lst)
