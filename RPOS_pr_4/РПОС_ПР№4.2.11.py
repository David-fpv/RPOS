
# Выполнил: Тарасенко Д.И.
# Группа: МС-32



def ceasar(text, shift):

    def Capital_symbol (letter, capital=True):
        letter = str(letter)
        if capital:
            return letter.upper()
        else:
            return letter.lower()

    letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]

    output_message = ''
    for symbol in text:
        capital_symbol = str(symbol).isupper()
        lower_symbol = str(symbol).lower()
        for i in range(len(letters)):
            if lower_symbol == letters[i]:
                i = (i + shift + len(letters)) % len(letters)
                output_message += Capital_symbol(letters[i], capital=capital_symbol)
                break
        else:
            output_message += symbol

    return output_message    


text = input("Введите предложение: ")
shift = int(input("Введите сдвиг: "))

encoded = ceasar(text, shift)
decoded = ceasar(encoded, -shift)
print("Зашифрованная строка:", encoded)
print("Расшифрованная строка:", decoded)

# --------------
# Пример вывода:
#
# Введите предложение: ПрограММиРОВание С++
# Введите сдвиг: 4
# Зашифрованная строка: УфтзфдРРмФТЖдсмй Х++
# Расшифрованная строка: ПрограММиРОВание С++
