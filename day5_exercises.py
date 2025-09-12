def fuel_efficiency(distance, fuel_used):
	km_per_liter = distance/fuel_used
	return km_per_liter

dist = int(input("Enter you distance in km: "))
fuel = int(input("Enetr fuel used in liters: "))

consumption = fuel_efficiency(dist, fuel)
print(f"Your consumption is {consumption}km/ltr...")