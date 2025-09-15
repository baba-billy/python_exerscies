class Account:

	def __init__(self, owner, balance = 0):
		self.owner = owner
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		if amount > self.balance:
			print("Insufficient funds")
		else:
			self.balance -= amount

	def check_balance(self):
		print(f"Your balance is {self.balance}")

class ATM:

	def __init__(self):
		self.account = None

	def insert_card(self, account):
		self.account = account

	def withdraw(self, amount):
		self.account.withdraw(amount)

	def deposit(self, amount):
		self.account.deposit(amount)

	def check_balance(self):
		self.account.check_balance()


acc = Account("Billy Ben", 25000)

gt_atm = ATM()
gt_atm.insert_card(acc)
gt_atm.deposit(50000)
gt_atm.withdraw(20000)
gt_atm.check_balance()