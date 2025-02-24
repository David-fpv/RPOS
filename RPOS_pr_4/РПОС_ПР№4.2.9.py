
# Выполнил: Тарасенко Д.И.
# Группа: МС-32



LETTERS_EX = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
DIGITS_EX = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}


def to_base(number, base):
    def append_symbol(number, value):
        if value < 10:
            number += str(value)
        else:
            number += str(LETTERS_EX.get(value))
        return number


    new_number_mirror = ""
    while True:
        if number < base:
            new_number_mirror = append_symbol(new_number_mirror, number)
            break
        
        new_number_mirror = append_symbol(new_number_mirror, number % base)
        number = number // base
        
    new_number = ""
    for i in new_number_mirror[::-1]:
        new_number += i
    return new_number



def from_base(number, base):

    def letter_to_int(symbol):
        if symbol.isdigit():
            return int(symbol)
        else:
            return int(DIGITS_EX.get(symbol))


    number_mirror = ""
    for i in number[::-1]:
        number_mirror += i

    new_number = 0
    for i in range(len(number_mirror)):
        new_number += letter_to_int(number_mirror[i]) * base**i

    return new_number


print(from_base("AA", 16))
print(to_base(255, 16))
# --------------
# Пример вывода:
#
# Нет
