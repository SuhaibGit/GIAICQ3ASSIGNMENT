def accessElement(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modifyElement(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def sliceList(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."

def indexGame():
    lst = [1, 2, 3, 4, 5]  # Example list
    print("Current list:", lst)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ")

    if operation == "access":
        index = int(input("Enter index to access: "))
        print(accessElement(lst, index))
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print(modifyElement(lst, index, new_value))
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(sliceList(lst, start, end))
    else:
        print("Invalid operation.")

indexGame()
