while (1):
    vehicleType = input(
        "Please enter a one of these vehicle types car, truck, plane, boat, or broomstick: ")
    vehicleType = vehicleType.capitalize()
    if vehicleType == "Car" or vehicleType == "Truck" or vehicleType == "Plane" or vehicleType == "Boat" or vehicleType == "Broomstick":
        break
    else:
        print("Invalid vehicle type")

yr = input("Please enter car year: ").capitalize()
mk = input("Please enter car make: ").capitalize()
mdl = input("Please enter car model: ").capitalize()
numDoors = input("Please enter number of doors for the car: ")
roofType = input("Please enter roof type solid or sun roof: ").capitalize()

# Normally I would do input validation for all of the user inputs but I didn't feel it was neccasary for this assignment
# Instead I just used input validation for the first user input.


class Vehicle:
    def __init__(self):
        self.type = vehicleType


class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__()
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def output(self):
        print("Vehicle type: " + self.type + "\nYear: " + self.year +
              "\nMake: " + self.make + "\nModel: " + self.model)
        print("Number of doors: " + "\nType of roof: " + self.roof)


userCar = Automobile(yr, mk, mdl, numDoors, roofType)

userCar.output()
