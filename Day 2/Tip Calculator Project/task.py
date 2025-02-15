print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n$"))
tip = int(input("What percentage tip would you like to give?\n"))
people = int(input("How many people to split the bill?\n"))
result = round(((bill + (bill * (tip/100))) / people), 2)
print(f"Each person will pay ${result}")

