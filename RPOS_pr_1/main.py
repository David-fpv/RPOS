import sys


russian_alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]
english_alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]


def Capital_symbol (letter, capital=True):
    letter = str(letter)
    if capital:
        return letter.upper()
    else:
        return letter.lower()


def Caesar_cipher (input_message, alpabet = english_alphabet, shift = 3, encypt = True):

    if encypt == False:
        shift = -1 * shift

    output_message = ''
    for symbol in input_message:
        capital_symbol = str(symbol).isupper()
        lower_symbol = str(symbol).lower()
        for i in range(len(alpabet)):
            if alpabet[i] == lower_symbol:
                i = (i + shift + len(alpabet)) % len(alpabet)
                output_message += Capital_symbol(alpabet[i], capital=capital_symbol)
                break
        else:
            output_message += symbol

    return output_message           




if (len(sys.argv)) != 5:
    print('There are not enough arguments for the program to work correctly.')

message = sys.argv[1]
shift = int(sys.argv[3])


alphabet = english_alphabet
if str(sys.argv[2]) in ['english', 'english_alphabet', 'en']:
    alphabet = english_alphabet
elif str(sys.argv[2]) in ['russian', 'russian_alphabet', 'ru']:
    alphabet = russian_alphabet


encrypt = True
if str(sys.argv[4]) in ['encrypt', '1', 'True']:
    encrypt = True
elif str(sys.argv[4]) in ['decrypt', '0', 'False']:
    encrypt = False


print(Caesar_cipher(message, alpabet=alphabet, shift=shift, encypt=encrypt))