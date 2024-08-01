class Motor:
    def __init__(self, size):
        self.size = size

    def describe_motor(self):
        return f"Tamaño motor: {self.size}"

class Auto:
    def __init__(self, brand, model, size):
        self.brand = brand
        self.model = model
        self.motor = Motor(size)

    def describe_motor(self):
        return self.motor.describe_motor()

car = Auto("Toyota", "RAV4", 2000)
print(car.describe_motor())
