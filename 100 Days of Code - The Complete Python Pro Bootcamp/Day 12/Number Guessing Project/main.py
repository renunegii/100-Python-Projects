import random
import art

print(art.logo)
def number_guess(chance, num):
    for i in range (0,chance):
        guess = int(input("Guess a number: "))
        if guess > num:
            print("Too High")
        elif guess < num:
            print("Too Low")
        elif guess == num:
            print(f"*** You guessed the right number {guess}. You Win! ***")
    else:
        print(f"*** You are out of Chances, Number was {num}, You Lose! ***")

#main program
print("*** Welcome to the number guessing game ***")
print("*** I'm thinking of a number between 1 to 100 ***")
number = random.randint(1,100)
choose = input("Choose the level of Game, Type 'h' for Hard and 'e' for Easy level")
if choose == 'h':
    chance = 5
else:
    chance = 10
number_guess(chance, number)