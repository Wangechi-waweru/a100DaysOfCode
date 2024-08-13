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
_________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to treasure Island.\nYour mission is to find the treasure.\n")

left_or_right = input('You\'re at a crossroad. Where do you want to go? "left(L)" or "right(R)"?\n ')
if left_or_right.upper() == "L":
    swim_or_wait = input('You\'ve come to a lake.'
                         'There is an island in the middle of the lake. '
                         'Will you "Swim(S)" or "Wait(W)"?\n ')
    if swim_or_wait.upper() == "W":
        door = input('You arrive at the island unharmed.'
                     'There\'s a house with three doors.'
                     'Which door will you open; "Red(R)", "Blue(B)" or "Yellow(Y)"?\n ')
        if door.upper() == "Y":
            print("You found the treasure! You win!")
        elif door.upper() == "R":
            print("This room is full of fire! You got burned! Game Over!")
        elif door.upper() == "B":
            print("This room is full of angry pirates! They shot you! Game Over! ")
        else:
            print("Oops! This door does not exit! Game Over!")
    else:
        print("You got attacked by a shark! Game Over!")
else:
    print("You fell into a well! Game Over!")




