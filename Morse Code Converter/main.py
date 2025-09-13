class InvalidMorseCodeError(Exception):
    """Exception for Incorrect Morse code"""
    pass

# ASCII art for program title
TITLE_ART = r"""
___  ___                      _____           _        _____                           _            
|  \/  |                     /  __ \         | |      /  __ \                         | |           
| .  . | ___  _ __ ___  ___  | /  \/ ___   __| | ___  | /  \/ ___  _ ____   _____ _ __| |_ ___ _ __ 
| |\/| |/ _ \| '__/ __|/ _ \ | |    / _ \ / _` |/ _ \ | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
| |  | | (_) | |  \__ \  __/ | \__/\ (_) | (_| |  __/ | \__/\ (_) | | | \ V /  __/ |  | ||  __/ |   
\_|  |_/\___/|_|  |___/\___|  \____/\___/ \__,_|\___|  \____/\___/|_| |_|\_/ \___|_|   \__\___|_|   

                                                                                                    """
# Morse Code Dictionary
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
                    'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
                    'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--',
                    'Z':'--..', '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....', '7':'--...',
                    '8':'---..', '9':'----.', '0':'-----', ',':'--..--',
                    '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# Invert Morse code dictionary to decode messages
INVERTED_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


print(TITLE_ART)
continue_converting = True

while continue_converting:

    # Ask user for operation type
    operation = ""
    while operation != "encode" and operation != "decode":
        operation = input("Choose operation, type: encode / decode:\n").strip().lower()

    input_text = input("Type message you want to encode/decode(Morse code letters should be separated with ' ' and words with '/'):\n").upper()
    output = ""

    # Prevent empty input
    if not input_text.strip():
        print("You entered an empty message.")
        continue

    # Encoding text into code
    if operation == "encode":
        try:
            for sign in input_text:
                if sign == " ":
                    output += "/ "
                else:
                    output += MORSE_CODE_DICT[sign] + " "
        except KeyError:
            print(f"Can't code sign: {sign}")
            output = ""

    # Decoding into text
    elif operation == "decode":
        try:
            words = [w.strip() for w in input_text.split("/")]
            for word in words:
                if not word.strip():
                    continue
                letters = word.split()
                for letter in letters:
                    if letter not in INVERTED_MORSE_CODE_DICT:
                        raise InvalidMorseCodeError(f"Incorrect Morse code: {letter}")
                    output += INVERTED_MORSE_CODE_DICT[letter]
                output += " "
        except InvalidMorseCodeError as error:
            print(error)
            output = ""

    else:
        print("You chose incorrect operation. Use 'encode' or 'decode'.")

    print(output.strip())

    # Ask if user wants to continue
    continue_text = ""
    while continue_text != "y" and continue_text != "n":
        continue_text = input("Do you want to continue? (y/n):\n").lower()
    if continue_text.lower() == "n":
        continue_converting = False
