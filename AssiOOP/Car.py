class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car has started.")

c = Car("Honda")
print(c.brand)
c.start()
