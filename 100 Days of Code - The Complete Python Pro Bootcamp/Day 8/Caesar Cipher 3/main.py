# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift, enc_or_dec):
    new_text = ""
    if enc_or_dec == "decode":
        shift *= -1
    for i in original_text:
        if i in alphabet:
            new_indx = alphabet.index(i) + shift
            new_indx %= len(alphabet)
            new_letter = alphabet[new_indx]
            new_text += new_letter
        else:
            new_text += i
    return new_text


# TODO-3: Can you figure out a way to restart the cipher program?
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    new_text = caesar(text, shift, direction)
    print(new_text)

    choice= input("Do you want to continue Y/N? ")
    if choice == "N" or choice == "n":
        print("Thank You!")
        break



