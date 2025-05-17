class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # public
        self._salary = salary     # protected
        self.__ssn = ssn          # private

e = Employee("Bob", 50000, "123-45-6789")
print(e.name)           
print(e._salary)       
# print(e.__ssn)        # Fails
print(e._Employee__ssn) 
