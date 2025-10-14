import random
import art

print(art.logo)

def play (cards):
    """Function to play Blackjack Game"""
    user_drawlst = []
    comp_drawlst = []
    user_sum = 0
    comp_sum = 0
    user_draw1 = random.choice(cards)
    user_draw2 = random.choice(cards)
    user_drawlst.append(user_draw1)
    user_drawlst.append(user_draw2)
    user_sum = user_draw1 + user_draw2

    comp_draw1 = random.choice(cards)
    comp_draw2 = random.choice(cards)
    comp_drawlst.append(comp_draw1)
    comp_drawlst.append(comp_draw2)
    comp_sum = comp_draw1 + comp_draw2

    print(f"Your cards = [{user_draw1}, {user_draw2}], Your Score = {user_draw1 + user_draw2}")
    print(f"Computer Card = [{comp_draw1}]")
    hit_or_stand = input("Type 'y' for hit or 'n' for stand: ")

    while True:
        if hit_or_stand == 'n':
            comp = random.choice(cards)
            comp_drawlst.append(comp)
            comp_sum += comp
            if comp_sum > 21:
                comp_sum = check_ace("Computer",comp_drawlst)
                if comp_sum > 21:
                    print(f"Your Cards = {user_drawlst}")
                    print(f"Your Final Score: {user_sum}, Computer's Final Score = {comp_sum}")
                    print(f"Computer is Over 21, You Win!")
                    break
            elif comp_sum < 17:
                continue
            else:
                break
            print(f"Computer Cards = {comp_drawlst} , Computer Score = {comp_sum}")

        else:
            user = random.choice(cards)
            user_drawlst.append(user)
            user_sum += user
            if user_sum > 21:
                user_sum = check_ace("You",user_drawlst)

            if user_sum > 21:
                print(f"Your Cards = {user_drawlst}")
                print(f"Your Final Score: {user_sum}, Computer's Final Score = {comp_sum}")
                print(f"You are Over 21, You Lose!")
                break
            print(f"Your Cards = {user_drawlst}, Your Score = {user_sum}")
            hit_or_stand = input("Type 'y' for hit or 'n' for stand: ")

    if comp_sum <= 21 and user_sum <= 21:
        if comp_sum < user_sum:
            print(f"Your Final Score: {user_sum}, Computer's Final Score = {comp_sum}")
            print(f"*** You Win! ***")
            return

        elif comp_sum > user_sum:
            print(f"Your Final Score: {user_sum}, Computer's Final Score = {comp_sum}")
            print(f"*** Computer Win! ***")
            return

        else:
            print(f"Your Cards = {user_drawlst} , Your Final Score = {user_sum}")
            print(f"Computer Cards = {comp_drawlst} , Computer Final Score = {comp_sum}")
            print("*** Match got Draw! ***")
            return

    else:
        return

def check_ace(user, drawlst):
    total = 0
    for i in range(len(drawlst)):
        if drawlst[i] == 11:
            drawlst[i] = 1
            print(f" {user} got an ace, {user}'s new Cards [{drawlst}]")
        total += drawlst[i]
    return total


#main program
deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]

game = input("Do you want to play Blackjack ? Type 'y' or 'n': ")
while game == 'y':
    play(deck)
    game = input("Type 'y' to play again and Type 'n' to end the game.")
    print("\n" * 20)