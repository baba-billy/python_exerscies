
file_name = "story.txt"

words = {}

with open(file_name, 'r') as file:
	content = file.read()
	# print(content)

remove_qoute = content.strip('"').lower()
list_of_words = remove_qoute.split()
for word in list_of_words:
	if word[-1] == '.':
		word = word[:-1]
	words[word] = words.get(word, 0) + 1

print(words)
# for word in content.lower().split():
# 	words[word] = words.get(word, 0) + 1

# print(words)	


# import csv

# with open('cars.csv', 'r') as csvfile:
# 		reader = csv.reader(csvfile)
# 		for row in reader:
# 			print(f"Brand: {row[0]} | Model: {1} | Year: {row[2]}")



# def store_items(item, price):
# 	val = f"\n{item}, {price}"
# 	try:
# 		with open('expenses.txt', 'a') as file:
# 			file.write(val)
# 	except FileNotFoundError:
# 		with open('expenses.txt', 'w') as file:
# 			file.write(val)


# def print_item():
# 	total = 0
# 	with open('expenses.txt', 'r') as file:
# 		val = file.readlines()
# 		for i in val:
# 			items = i.split()
# 			total += int(items[1])
# 			print(items[0], items[1])
# 		print(total)


# input_item = input("Enter Item you select: ")
# if input_item.lower() == "report":
# 	print_item()
# else:
# 	price_input = input("Enter price of item selected: ")
# 	store_items(input_item, price_input)
# # store_items("mango", 500)
