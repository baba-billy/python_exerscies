# def safe_divide(a, b):
# 	try:
# 		return a/b
# 	except ZeroDivisionError:
# 		return "Cannot divide by Zero"

# def read_file(file_name):
# 	try:
# 		with open(file_name, 'r') as file:
# 			content = file.read()
# 			return content
# 	except FileNotFoundError:
# 		return "File not found!"


# try:
# 	num_val = int(input("Enter a number: "))
# 	num_squared = num_val ** 2
# 	file_val = input("Input File Name: ")
# 	with open(file_val) as file:
# 		content = file.read()
# 	print(num_squared, content)
# except ValueError:
# 	print("Invalid Number")
# except FileNotFoundError:
# 	print("File not found")

# class NegativeNumberError(Exception):

# 	def __init__(self, message):
# 		self.message = message
# 		super().__init__(self.message)

# def square_root(a):
# 	if a < 0:
# 		raise NegativeNumberError("Cannot find Square root of negative number.")
# 	return a ** 0.5

# try:
# 	result = square_root(-9)
# 	print(result)
# except NegativeNumberError as e:
# 	print(e)


# try:
# 	price = int(input("Enetr amount: "))
# 	if price == 0:
# 		print("Input cannot be empty")
# 	else: print("The code will work")
# except ValueError:
# 	print("Amount must be in number")


#ATM Simulator#

balance = 50000

try:
	withdraw = int(input("Enter amount you want to withdraw: "))
	if withdraw > balance:
		print("Insufficient funds")
	elif withdraw < 0:
		print("Cannot withdraw negative amount")
	else:
		balance -= withdraw
		print(f"You have withdrawn {withdraw}, your balance is {balance}")	
except ValueError:
	print("Invalid Input")

