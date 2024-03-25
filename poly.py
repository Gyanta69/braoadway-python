class Car:
    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model
    def move(self):
         print("Car created")

class Plane:
    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model
    def move(self):
         print("Plane created")

class Boat:
    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model
    def move(self):
         print("Boat created")

car1 =Car("test","tesla")
plane1 = Plane("Boat brand","test")
boat1 = Boat("Plane brand   ","test")

print(car1.move())
for data in(car1,plane1,boat1):
    data.move()


# inheritance
class Vehicle:
    def __init__(self,brand,model) -> None:
        self.brand = brand
        self.model = model
    def move(self):
         print("Move")