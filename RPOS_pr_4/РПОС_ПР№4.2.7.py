
# Выполнил: Тарасенко Д.И.
# Группа: МС-32



def has_digits(sentence):
    for symbol in sentence:
        if symbol.isdigit():
            return True
    return False


def sentences_with_digits_count(sentences):
    counter = 0
    for sentence in sentences:
        if has_digits(sentence):
            counter += 1
    return counter


n = int(input("Введите количество предложений: "))
sentences = list()
for i in range(n):
    sentences.append(input(f"Введите предожение №{i+1}:\n"))

print(f"Предложений с цифрой = {sentences_with_digits_count(sentences)}")

# --------------
# Пример вывода:
#
# Введите количество предложений: 3
# Введите предложение №1:
# Просто текст
# Введите предложение №2:
# Текст с цифрой 1 (один)
# Введите предложение №3:
# Тут нет цифры
# Предложений с цифрой = 1
