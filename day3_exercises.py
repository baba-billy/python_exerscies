mileage = []

for i in range(1, 6):
    mile = int(input(f"Enter mileage for day {i}: "))
    mileage.append(mile)

total = 0
for i in mileage:
    total += i

print(total, total/len(mileage))


