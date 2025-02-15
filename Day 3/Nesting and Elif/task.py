print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Enter your age: "))
    if age < 12:
        print("Kindly pay $5")
    elif age >= 12 and age < 18:
        print("Kindly pay $7")
    else:
        print("Kindly pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")
