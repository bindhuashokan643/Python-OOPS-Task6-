#Vehicle Rental

class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental_rate(self, days):
        return self.rental_rate * days


#Subclass: Car

class Car(Vehicle):
    def __init__(self, model, rental_rate, seats):
        super().__init__(model, rental_rate)
        self.seats = seats

    def calculate_rental_rate(self, days):
        return self.rental_rate * days


#Subclass : Bike

class Bike(Vehicle):
    def __init__(self, model, rental_rate, bike_type):
        super().__init__(model, rental_rate)
        self.bike_type = bike_type

    def calculate_rental_rate(self, days):
        return self.rental_rate * days

#Subclass: Truck
class Truck(Vehicle):
    def __init__(self, model, rental_rate, load_capacity):
        super().__init__(model, rental_rate)
        self.load_capacity = load_capacity

    def calculate_rental_rate(self, days):
        return self.rental_rate * days

Vehicles = [
    Car("Honda Cit", 1000, 5),
    Bike("Yamaha", 500, "Sports"),
    Truck("Tat", 2000, "10 Tone")
]
days = 5

for v in Vehicles:
    print(f"{v.model} Rental Cost for {days} day: {v.calculate_rental_rate(days)}")
