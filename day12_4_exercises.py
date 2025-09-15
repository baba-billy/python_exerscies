class Car:

	def __init__(self, owner, brand, mileage, issues = []):
		self.owner = owner
		self.brand = brand
		self.mileage = mileage
		self.issues = issues

	def report_issue(self, issue):
		self.issues.append(issue)


class Mechanic:

	def __init__(self, name, specialization):
		self.name = name
		self.specialization = specialization

	def fix_car(self, car):
		car.issues.clear()
		print("All your car issues has been fixed")


vehicle_issue = ["Battery", "Emgine oil", "gear oil"]

car1 = Car("Billy", "BMW", 23488, vehicle_issue)
mechanic1 = Mechanic("Kabir", "HVAC")
car1.report_issue("brake oil")

# mechanic1.fix_car(car1)
print(car1.issues)