def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2


operations = {"+": add,
              "-": sub,
              "*": multiply,
              "/": divide}
def calculate():
    sol = 0
    n1 = float(input("What's the first number? "))

    while True:
        for symbol in operations:
            print(symbol)
        opr = input("Choose the operations: ")
        n2 = float(input("What's the second number? "))

        if opr == "+":
            sol = add(n1, n2)

        elif opr == "-":
            sol = sub(n1, n2)

        elif opr == "*":
            sol = multiply(n1, n2)

        elif opr == "/":
            sol = divide(n1, n2)

        else:
            print("You have entered a wrong operation.")

        print(f"{n1} {opr} {n2} = {sol}")
        choice = input("Type 'y' to continue calculating with previous calculation, \n"
                       "or type 'n' to start a new calculation: \n"
                       "or type 'break' to end the calucations  \n")

        if choice == "y":
            n1 = sol
        elif choice == "n":
            calculate()
        else:
            print("Thanks for using!")
            break

calculate()