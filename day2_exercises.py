consumption = int(input("Enter the fuel consumption in liters per 100 km: "))

if consumption <= 6:
    print("Excellent fuel efficiency.")
elif 7 <= consumption <= 10:
    print("Average fuel efficiency.")
else:
    print("Poor fuel efficiency. Consider a check up.")
    