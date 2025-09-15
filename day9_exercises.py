# vin = input("Enter Your vehicle vin: ")

# def vin_validator(vin):
# 	if len(vin) == 17:
# 		if "I" not in vin.upper() and "O" not in vin.upper() and "Q" not in vin.upper():
# 			print("Valid VIN")
# 		else: print("Invalid VIN")
# 	else: print("Invalid VIN")

# vin_validator(vin)



# def is_palindrome(word):
# 	if word == word[::-1]:
# 		print(word[::-1], True)
# 	else: print(word, False)

# is_palindrome("madam")


# sentence = "car car bus bike car"
# list_of_words = sentence.split()
# no_of_words = {}

# for words in list_of_words:
# 	no_of_words[words] = no_of_words.get(words, 0) + 1 

# print(no_of_words)

# password = input("Input password: ")

# def true_or_flase(val):
# 	if val:
# 		return "Present"
# 	else:
# 		return "Not Present"

# def password_checker(password):

# 	pass_condition = {"length_greater_than_8": False,
# 					  "contains_digit": False,
# 					  "contains_uppercase": False,
# 					  "contains_special_character": False
# 	}
# 	if len(password) >= 8:
# 		pass_condition["length_greater_than_8"] = True
# 		for char in password:
# 			if char.isdigit():
# 				pass_condition["contains_digit"] = True
# 			if char.isupper():
# 				pass_condition["contains_uppercase"] = True
# 			if not char.isalnum():
# 				 pass_condition["contains_special_character"] = True

# 		return pass_condition
# 	else:
# 		return {}
# pass_result = password_checker(password)
# if pass_result == {}:
# 	print("Password is too short. It should be at least 8 characters")
# else:
# 	if pass_result["contains_digit"] == True and pass_result["contains_uppercase"] == True and pass_result["contains_special_character"] == True:
# 		print("Strong password")
# 	else:
# 		print(f"""Password is Weak,
# UpperCase: {true_or_flase(pass_result["contains_uppercase"])}
# Digit: {true_or_flase(pass_result["contains_digit"])}
# Special Character: {true_or_flase(pass_result["contains_special_character"])} 
# 		 	 """)

# # print(pass_result)



number_plate = "abc1234"

letters = number_plate[:3]
numbers = number_plate[3:]

if len(letters) == 3 and letters.isalpha():
	if len(numbers) == 4 and numbers.isdigit():
		print(f"Plate Number: {letters.upper()} {numbers}")
else:
	print("Invalid Plate")

# print(letters, numbers)

