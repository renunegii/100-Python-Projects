import random

def who_won(x,y):
    if x==y:
        print("Match is draw")

    elif x==rock:
        if y==paper:
            print("Computer Won")
        elif y==scissors:
            print("You Won")

    elif x==paper:
        if y==scissors:
            print("Computer Won")
        elif y==rock:
            print("You Won")

    elif x==scissors:
        if y==rock:
            print("Computer Won")
        elif y==paper:
            print("You Won")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
l=[rock,paper,scissors]
# comp = random.choice([rock, paper, scissors])
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
comp= random.randint(0,2)
print(f"You chose: \n {l[choice]}")
print(f"Computer chose: \n {l[comp]}")
# if choice==0:
#     print(f"You chose\n {rock}")
#     print(f"Computer chose\n {comp}")
#     print(who_won(rock,comp))
#
# elif choice==1:
#     print(f"You chose\n {paper}")
#     print(f"Computer chose\n {comp}")
#     print(who_won(paper,comp))
#
# elif choice==2:
#     print(f"You chose\n {scissors}")
#     print(f"Computer chose\n {comp}")
#     print(who_won(scissors,comp))
#
# else:
#     print("Invalid Choice")
if choice==comp:
    print("The match is draw")
elif choice==0:
    if comp==1:
        print("Computer won")
    elif comp==2:
        print("You Won")
elif choice==1:
    if comp==2:
        print("Computer won")
    elif comp==0:
        print("You Won")
elif choice==2:
    if comp==0:
        print("Computer won")
    elif comp==1:
        print("You Won")

else:
    print("Invalid choice")