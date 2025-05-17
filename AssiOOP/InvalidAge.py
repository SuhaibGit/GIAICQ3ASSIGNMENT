class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    print("Access granted.")

try:
    print("Age set to 20")
    check_age(20)
    print("Age set to 16")
    check_age(16)
except InvalidAgeError as e:
    print("Error:", e)
