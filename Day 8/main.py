from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
end = False


def encode(shift, text):
    answer = ''
    for letters in text:
        new_index = alphabet.index(letters) + shift
        answer += alphabet[new_index]

    return print(answer)
def decode(shift, text):
    answer = ''
    for letters in text:
        new_index = alphabet.index(letters) - shift
        answer += alphabet[new_index]

    return print(answer)


while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encode(shift, text)
    elif direction == "decode":
        decode(shift, text)
    else:
        pass
    if input("do you want to start again yes or no?").lower() == "yes":
        pass
    else:
        end = True