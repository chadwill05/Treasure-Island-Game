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



print("There will be a lot of twists and turns so be careful!")
choice1 = input("On your journey, the path forks into two ways, which way are you taking? Type left or right.  ").lower()

if choice1 == "left":
  choice2 = input("Good Job! You took the correct turn. To keep going you have to cross a big lake. Will you wait for a boat or swim across? Type wait or swim.  ").lower()
  if choice2 == "wait":
    choice3 = input("Thank God you waited. A yacht with some supplies came to your rescue! Now you can smell the treasure! On the way you will see a house with three doors. One red, yellow and blue. Which door will you choose?  ").lower()
    if choice3 == "red":
      print("Sorry! There were 3 rabbid dogs and one of them bit you. Game over!")
    elif choice3 == "blue":
      print("Congrats! You found the treasure! Now you can go back on the yacht and party!")
    elif choice3 == "yellow":
      print("The gold was no where to be found and a trap door was hidden underneath your step that unfortunately brought upon your death.")
    else:
      print("You chose the wrong door! Game over!")
  else:
    print("O no! A shark bit your leg. You are dead! Game over!")
    
else:
  print("Wrong choice! You are dead. Game over.")

