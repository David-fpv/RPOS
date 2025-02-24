
# Выполнил: Тарасенко Д.И.
# Группа: МС-32



def print_with_border(string, char):
    print(char * (len(string) + 2))
    print(char + string + char)
    print(char * (len(string) + 2))


s = input("Введите строку: ")
k = input("Введите символ: ")
print_with_border(s, k)

# --------------
# Пример вывода:
#
# Введите строку: Просто текст
# Введите символ: +
# ++++++++++++++
# +Просто текст+
# ++++++++++++++
