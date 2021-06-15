print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("There is a fork in the path before you. Do you go *left* or *right*?\n").lower()
if direction == "left":
    print("You head down the left path, down to the shore.")
    
    lake = input("You have to cross a lake to a small island. Do you *swim* across or *wait* for a boat?\n").lower()
    if lake == "wait":
        print("A ferry arrives shortly to take you across. You arrive on the island in front of a grand mansion.")
        
        door = input("There are three doors before you, do you enter through the *red*, *yellow*, or *blue* one?\n").lower()
        if door == "yellow":
            print("You chose correctly and enter to a giant vault of riches. You win!")
        elif door == "red":
            print("You enter a brick room with odd looking grates in the floor. The door locks behind you and flames shoot up. Game over.")
        elif door == "blue":
            print("You enter a room full of caged beasts. Only on second inspection do you notice that none of them are locked. Game over.")

    else:
        print("Halfway across the lake, a fin breaks the surface of the water. You are swiftly gobbled up. Game over.")
else:
    print("You find yourself in an endless maze and become lost for the rest of your days. Game over.")