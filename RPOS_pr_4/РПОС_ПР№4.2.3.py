
# Выполнил: Тарасенко Д. И.
# Группа: МС-32



def is_lucky(num):
    symbols = list(str(num))
    even_numbers = 0
    for i in symbols:
        if int(i) % 2 == 0:
            even_numbers += 1
    
    if len(symbols) // 2 == even_numbers:
        return True
    else:
        return False

def lucky_numbers(a, b):
    lucky_tikets = list()
    
    for i in range(a, b+1):
        if is_lucky(i):
            lucky_tikets.append(i)

    return lucky_tikets

a = int(input("Первый номер билета: "))
b = int(input("Последний номер билета: "))

lucky_tickets = lucky_numbers(a, b)
for i in range(len(lucky_tickets)):
    if i != len(lucky_tickets):
        print(lucky_tickets[i], end=' ')
    else:
        print(lucky_tickets[i])

# --------------
# Пример вывода:
#
# Первый номер билета: 10
# Последний номер билета: 25
# 10 12 14 16 18 21 23 25
