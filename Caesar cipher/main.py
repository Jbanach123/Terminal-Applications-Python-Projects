from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(message, number, cdirection):
    number = number % 26
    caesar_text = ""
    # Check direction
    if cdirection == "decode":
        number *= -1
    # Make a shift
    for char in message:
        if char in alphabet:
            old_position = alphabet.index(char)
            new_position = alphabet[old_position + number]
            caesar_text += new_position
        else:
            caesar_text += char
    print(f"Your {cdirection}d message is  {caesar_text}\n")


print(logo)
should_continue = True
while should_continue:
    # Choose direction message and shift
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(message=text, number=shift, cdirection=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type'no'.\n ")
    if restart == "no":
        should_continue = False
        print("\nGoodbye")
