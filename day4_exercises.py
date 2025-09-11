maintenance_task = ["Oil change", "Tire rotation", "Brake check", "Battery test", "AC check"]

def print_list(list):	
	for i in range(len(list)):
		print(f"{i+1}. {list[i]}")
		

print_list(maintenance_task)
val = int(input("Which task(1-5) has been completed: "))
maintenance_task.remove(maintenance_task[val-1])
print_list(maintenance_task)

