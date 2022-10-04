#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#
class Vehicle():
    def __init__(self, bodyStyle):
        self.bodyStyle = bodyStyle

    def drive(self, speed):
        self.mode = "Driving"
        self.speed = speed


class Car(Vehicle):
    def __init__(self, engineType):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.engineType = engineType

    def drive(self, speed):
        super().drive(speed)
        print(f"Driving my {self.engineType} car at {self.speed}mph")


class Motorycycle(Vehicle):
    def __init__(self, engineType, hasSideCar):
        super().__init__("Motorcycle")
        if hasSideCar == True:
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.engineType = engineType


car1 = Car("gas")
car2 = Car("diesel")
motorcycle1 = Motorycycle("electric", False)

print(car1.bodyStyle)
print(car2.doors)
print(motorcycle1.wheels)
print(car2.drive(42))
