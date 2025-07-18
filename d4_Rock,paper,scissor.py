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
    print("Invalid choice, So Computer Won by default")
random_choice=random.randint(0,2)

if(random_choice==0):
    print(''' Computer Choosed rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif random_choice==1:
    print('''Computer Choosed Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

elif(random_choice==2):
    print('''Computer Choosed Scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

if(n==0 and random_choice==0 or n==1 and random_choice==1 or n==2 and random_choice==2):
    print("It's a draw")
elif(n==0 and random_choice==2 or n==1 and random_choice==0 or n==2 and random_choice==1):
    print("You Won")
else:
    print("Computer Won")
    


    

    










