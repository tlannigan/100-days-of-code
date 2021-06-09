# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
max_lived = lambda x: x * 90

days_lived = int(age) * 365
weeks_lived = int(age) * 52
months_lived = int(age) * 12

days_left = max_lived(365) - days_lived
weeks_left = max_lived(52) - weeks_lived
months_left = max_lived(12) - months_lived

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")