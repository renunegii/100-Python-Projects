import random
import art
from game_data import data
print(art.logo)

def compare(guess, a_part, b_part):
    if a_part["follower_count"] > b_part["follower_count"]:
        result = 'a'
    else:
        result = 'b'
    if guess == result:
        return True
    else:
        return False

def format_data(a_part, b_part):
    print(f"Compare"
          f" A -> {a_part["name"]}, a {a_part["description"]}, in {a_part["country"]}")
    print(art.vs)
    print(f"B -> {b_part["name"]}, a {b_part["description"]}, in {b_part["country"]}")

#main program
account_2 = random.choice(data)
score = 0
while True:
    account_1 = account_2
    if account_1 == account_2:
        account_2 = random.choice(data)
    format_data(account_1, account_2)
    guess = input("Guess who has more followers, Type 'A' or 'B': ").lower()
    result = compare(guess, account_1, account_2)
    if result:
        score += 1
        print(f"You are right, Your Score is {score}")
    else:
        print(f"You are wrong, Your Final score is {score}")
        break