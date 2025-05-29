print("Welcome to python pizza deliveries")
total_cost = 0
size = input("What size pizza do you want? S, M or L: \n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n")
extra_cheese = input("Do you want extra cheese? Y or N: \n")

if size == "S":
    total_cost += 15
elif size == "M":
    total_cost += 20
elif size == "L":
    total_cost += 25
else:
    print("You entered wrong values. ")

if pepperoni == "Y":
    if size == "S":
        total_cost += 2
    else:
        total_cost += 3

if extra_cheese == "Y":
    total_cost += 1

print(f"Checkout price : ${total_cost}")

print("Welcome to the rollercoaster! ")
height = int(input("What is your height in cm? \n"))
age = int(input("What is your age in years? \n"))
if height >= 120:
    if age >= 18:
        print("Adult tickets are 12$")
        cost = 12
    elif age <= 12:
        print("Youth tickets are 5$")
        cost = 5
    else:
        print("Child tickets are 7$")
        cost = 7

    wants_photo = input("Do you want a photo taken? y for Yes and n for No\n")
    if wants_photo == "y":
        cost += 3
        print(f"Total cost will be {cost}$")
else:
    print("You are too short...")

print("Check whether input is even or odd . ")
number = int(input("Input a number .\n"))
if number % 2 == 0:
    print("It is an even number.")
else:
    print("It is an odd number.")