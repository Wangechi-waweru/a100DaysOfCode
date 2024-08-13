print("Welcome to the tip calculator!\n")

bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
total_pay = bill * (1 + (tip / 100))

no_of_people = int(input("How many people to split the bill?"))
each_person_pays = round(total_pay / no_of_people, 2)

print(f"Each person should pay: ${each_person_pays}")
