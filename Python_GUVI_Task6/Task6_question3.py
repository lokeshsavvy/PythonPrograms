class Vehicle:
    def __init__(self,model,rental_rate):
        self.model = model
        self.rental_rate = rental_rate
class Car(Vehicle):
    def __init__(self,model,rental_rate,days):
        super().__init__(model,rental_rate)
        self.days = days
    def calculate_rental(self):
        return self.rental_rate * self.days
class Bike(Vehicle):
    def __init__(self,model,rental_rate,hours):
        super().__init__(model,rental_rate)
        self.hours = hours
    def calculate_rental(self):
        return self.rental_rate * self.hours
class Truck(Vehicle):
    def __init__(self,model,rental_rate,distance,load):
        super().__init__(model,rental_rate)
        self.distance = distance
        self.load = load
    def calculate_rental(self):
        return self.distance * self.load * self.rental_rate

#creating object and taking inputs from the user

vechicle_type = input("Enter the vehicle type: ").lower()
if vechicle_type == 'car':
    model = input("Enter the car model you want: ")
    days = int(input("how many days: "))
    rental_rate = int(input("Enter the rate: "))
    obj = Car(model,rental_rate,days)
elif vechicle_type == 'bike':
    model = input("Enter the bike model you want: ")
    hours = int(input("How many hours: "))
    rental_rate = int(input("Enter the rate: "))
    obj = Bike(model,rental_rate,hours)
elif vechicle_type == 'truck':
    model = input("Enter the truck model you want: ")
    rental_rate = int(input("Enter the rental rate: "))
    distance = int(input("Enter the distance: "))
    load = int(input("Enter the load in weight: "))
    obj = Truck(model,rental_rate,distance,load)
else:
    print("Vechicle type not available")

if vechicle_type in ['car', 'bike', 'truck']:
    print(obj.calculate_rental())

        



