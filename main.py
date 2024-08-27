#Ceaser cipher
from art import logo
from text import alphabet
print(logo)

def ceaser(start_text, shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"the{cipher_direction}d text is {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt,type 'decode' to decrypt: \n").lower()

    text = input("enter your text: ").lower()
    shift = int(input("enter shift amount: "))
    shift = shift % 26

    ceaser(start_text=text,shift_amount=shift,cipher_direction=direction)
    restart = input("Type 'Yes' if you want to go again otherwise type 'no' .\n")
    if restart == 'no':
        should_continue = False
        print("Goodbye")
