#
# Выполнил: Тарасенко Д. И.
# Группа: МС-32



def sgn(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

x = int(input("Введите x: "))

y = int(input("Введите y: "))

z =  (sgn(x) + y**2) / (sgn(y) - abs(x)**0.5)

print(f"Ответ: {z:.2f}")

# --------------
# Пример вывода:
#
# Введите x: -9
# Введите y: 0
# Ответ: 0.33
