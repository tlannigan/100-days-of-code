# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
if (len(str(two_digit_number)) <= 2):
    first_number = int(two_digit_number[0])
    second_number = int(two_digit_number[1])
    print(first_number + second_number)
else:
    exit("You did not enter a two digit number. Re-run the program and try again.")