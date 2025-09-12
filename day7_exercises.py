
# List of Services in dictionary
services = {
    "Oil change": 15000,
    "Tire rotation": 8000,
    "Brake check": 12000,
    "Battery test": 10000
}

selected_service = [] # List of Services selected
total = 0 # to initiate Total cost of services

def display_services(services):
	""" This diplays the services offered by 
		looping through the dictionary using enumerate
	"""
	print("Our Services")
	for i, (j, k) in enumerate(services.items()):
		print(f"{i + 1}. {j}  --->  {k}")

display_services(services) # Function call to display service

# To get number of service required
no_of_services = int(input("How many services do you want to do: "))

# To ask for the services need and stores in 'selected_service' variable
for i in range(no_of_services):
	chosen_service = int(input("Which service do you want, select using numbers: "))
	selected_service.append(chosen_service)

# Gets list of "services" dictionary key 
services_keys = list(services.keys())

# Prints selected services and total
print("--- Service Receipt ---")
for i in selected_service:
	task = services_keys[i-1]
	cost = services[services_keys[i-1]]
	total += cost
	print(f"{task} : {cost}")
print(f"Total : {total}")
print("Thank you for choosing us!")