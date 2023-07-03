class Vehicle:
    def Into(self):
        print("There are different Vehicles")
    def Speed(self):
        print("Different cars has different speed")  

class Truck(Vehicle):
    def Speed(self):
        print("This is Slow Speed")

class Car(Vehicle):
    def Speed(self):
        print("This is Faster")

Vec = Vehicle()
Car = Car()
Tru = Truck()

Vec.Into()
Vec.Speed()
print("-----------------")

Car.Into()
Car.Speed()
print("-----------------")

Tru.Into()
Tru.Speed()
print("-----------------")