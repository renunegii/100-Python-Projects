try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have entered a wrong value, please try with a number like- 12. ")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
