# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
size = size.lower()
add_pepperoni = add_pepperoni.lower()
extra_cheese = extra_cheese.lower()

bill = 0
if size == "s":
    bill = 15
    if add_pepperoni == "y":
        bill += 2
elif size == "m":
    bill = 20
    if add_pepperoni == "y":
        bill += 3
elif size == "l":
    bill = 25
    if add_pepperoni == "y":
        bill += 3
else:
    bill = 20
    if add_pepperoni == "y":
        bill += 3
    print("We didn't understand what size you wanted, so you're getting a medium pizza :)")

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")