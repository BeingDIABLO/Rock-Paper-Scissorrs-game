import random

rock = '''Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_icons=[rock, paper, scissors]
user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if(user_input>=3 or user_input<=-1):
    print("Invalid choice, So Computer Won by default")
else:
    print(f"You choose",game_icons[user_input])

    
computer_choice=random.randint(0,2)
print(f"Conpter Choose",game_icons[computer_choice])

if(user_input==0 and computer_choice==0 or user_input==1 and computer_choice==1 or user_input==2 and computer_choice==2):
    print("It's a draw")
elif(user_input==0 and computer_choice==2 or user_input==1 and computer_choice==0 or user_input==2 and computer_choice==0):
    print("You Won")
else:
    print("Computer Won")
    
