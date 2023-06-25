def game_start():
    
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
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
    '''
)

    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()
    if choice1 == "right":
        print("You fell into a hole! Game Over.")
    elif choice1 == "left":
        choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
        if choice2 == "swim":
            print("You've drown. Game Over.")
        elif choice2 == "wait":
            print("You got on the boat and found the treasure")
            print("You win!")
        else:
            print(input("Game Reset. No valid choices were made. Enter anything to start over."))
            game_start()
    else:
        print(input("Game Reset. No valid choices were made. Enter anything to start over."))
        game_start()

game_start()