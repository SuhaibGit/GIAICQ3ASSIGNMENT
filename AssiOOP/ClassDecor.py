def add_greeting(cls):
    class Wrapped(cls):
        def greet(self):
            return "Hello from Decorator!"
    return Wrapped

@add_greeting
class Person:
    pass

p = Person()
print(p.greet())
