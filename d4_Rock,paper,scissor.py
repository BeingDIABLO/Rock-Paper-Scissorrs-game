import random
n=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if n==0:
    print(''' You Choosed rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif n==1:
    print('''You Choosed Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

elif n==2:
    print('''You Choosed Scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
else:
    print("Invalid choice")
random_choice=random.randint(3,5)

if(random_choice==3):
    print(''' Computer Choosed rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif random_choice==4:
    print('''Computer Choosed Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

elif(random_choice==5):
    print('''Computer Choosed Scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

if(n==0 and random_choice==3 or n==1 and random_choice==4 or n==2 and random_choice==5):
    print("It's a draw")
elif(n==0 and random_choice==5 or n==1 and random_choice==3 or n==2 and random_choice==4):
    print("You Won")
else:
    print("Computer Won")
    


    

    










