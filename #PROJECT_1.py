#project_1_treasure_island
print ('''
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
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
\n\n\n\n\n''')
choice = 3
print ("Welcome to Treasure Island!\nYour mission is to find the treasure")
while choice != 0:
    choice = 3
    direction= input ("Left or Right? \n")
    if direction == "left" or direction == "LEFT" or direction == "Left" :
        action = input ("Swim or wait? \n")
        if action == "wait" or action == "WAIT" or action == "Wait":
            door = input ("Which door colour? \n")
            if door == "YELLOW" or door == "yellow" or door == "Yellow":
                print ("You win! congratulations")
            else:
                if door == "Blue" or door == "BLUE" or door == "blue":
                    print ("Eaten by beasts! GAME OVER!!!!!!!!!")
                elif door == "Red" or door == "RED" or door == "RED":
                    print ("Burnt by fire! GAME OVERRRR!!!!!!!!")
                else:
                    print ("GAME OVER!!!!!!!!!!!!!")
        else:
            print ("Shit! Attacked by a Trout! GAME OVER!!!!!!!!!")
    else:
        print ("Opps! You fell into a hole! GAME OVER!!!!!!!!!!")
    while choice == 3:
        ch = input ("Do you want to continue? press y for yes and n for no \n")
        if ch == 'y' or ch == 'Y':
            choice = 1
        elif ch == 'n' or ch == 'N':
            choice = 0
        else:
            choice = 3
            print ("Wrong Choice! \n")