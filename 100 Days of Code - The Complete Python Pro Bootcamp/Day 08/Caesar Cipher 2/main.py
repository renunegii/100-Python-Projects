
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def encrypt(original_text, shift, enc_or_dec):
    new_text = ""
    if enc_or_dec == "decode":
        shift *= -1
    for i in original_text:
        new_indx = alphabet.index(i) + shift
        new_indx %= len(alphabet)
        new_letter = alphabet[new_indx]
        new_text += new_letter
    return new_text

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    new_text = encrypt(text, shift, direction)
    print(new_text)

    choice= input("Do you want to continue Y/N? ")
    if choice == "N":
        print("Thank You!")
        break