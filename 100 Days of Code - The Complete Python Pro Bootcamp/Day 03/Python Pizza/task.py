print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
money=0
if size == "S":
    money+=15
    if pepperoni == "Y":
        money+=2
    if extra_cheese == "Y":
        money+=1

elif size=="M":
    money+=20
    if pepperoni == "Y":
        money+=3
    if extra_cheese == "Y":
        money+=1

elif size=="L":
    money+=25
    if pepperoni == "Y":
        money+=3
    if extra_cheese == "Y":
        money+=1

print(f"Your final bill is: ${money}.")