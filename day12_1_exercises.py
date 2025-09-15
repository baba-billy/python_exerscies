class Vehicle:

	def __init__(self, brand, model, year):
		self.brand = brand
		self.model = model
		self.year = year

	def display_info(self):
		print(f"{self.brand}, {self.model}, {self.year}")

class Car(Vehicle):
	
	def __init__(self, brand, model, year, num_doors):
		super().__init__(brand, model, year)
		self.num_doors = num_doors

	def display_info(self):
		print(f"{self.brand}, {self.model}, {self.year}, {self.num_doors}")

class Truck(Vehicle):
	
	def __init__(self, brand, model, year, payload_capacity):
		super().__init__(brand, model, year)
		self.payload_capacity = payload_capacity

	def display_info(self):
		print(f"{self.brand}, {self.model}, {self.year}, {self.payload_capacity}")

class Bus(Vehicle):
	
	def __init__(self, brand, model, year, passenger_capacity):
		super().__init__(brand, model, year)
		self.passenger_capacity = passenger_capacity
	
	def display_info(self):
		print(f"{self.brand}, {self.model}, {self.year}, {self.passenger_capacity}")



my_vehicle = Vehicle("Airbus", "A50", 2020)
my_vehicle.display_info()

my_car = Car("Audi", "R8", 2020, 2)
my_car.display_info()

my_truck = Truck("Scannia", "cruiser", 2012, 50000)
my_truck.display_info()

my_bus = Bus("Hongchi", "packer", 2016, 50)
my_bus.display_info()