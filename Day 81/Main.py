MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '/'}
print("Hello, Welcome to Morse Code Translator")


def encrypt():
    message = input("Please Enter the text that you would like to encrypt ").upper()
    t_message = ""
    for letter in message.upper():
        t_message += f"{MORSE_CODE_DICT[letter]} "
    print(t_message)


def decrypter():
    message = input("Please Enter the text that you would like to decrypter ")
    t_message = ""
    message = message.split()
    for letter in message:
        for key, value in MORSE_CODE_DICT.items():
            if letter == value:
                t_message += key
    print(t_message)


if input("What Would You Like To Do encrypt or decrypter ").lower() == "encrypt":
    encrypt()
else:
    decrypter()
