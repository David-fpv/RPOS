
# Выполнил: Тарасенко Д.И.
# Группа: МС-32



def sentence_stats(sentence):
    sentence = sentence.lower()
    statistic = dict()

    for i in sentence:
        if i in statistic:
            statistic[i] += 1
        else:
            statistic[i] = 1

    return statistic


s = input("Введите предложение: ")
print(sentence_stats(s))

# --------------
# Пример вывода:
#
# Введите предложение: мама МЫла РамУ
# {'л': 1, 'р': 1, 'у': 1, 'м': 4, 'а': 4, 'ы': 1, ' ': 2}
