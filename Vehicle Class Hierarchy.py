
class Vehicle:
    def describe(self):
        return "This is a vehicle."

class Car(Vehicle):
    def describe(self):
        return "This is a car."

class Bike(Vehicle):
    def describe(self):
        return "This is a bike."

# Example usage
vehicles = [Car(), Bike()]
for vehicle in vehicles:
    print(vehicle.describe())