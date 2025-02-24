
# Выполнил: Тарасенко Д.И.
# Группа: МС-32



def is_leap(year):
    if year % 4 != 0:
        return False

    if year % 100 != 0:
        return True

    if year % 400 == 0:
        return True
    else:
        return False


def days(month, year):
    list_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 29]

    if is_leap(year) and month == 2:
        return list_months[13-1]
    
    return list_months[month-1]


def previous_date(day, month, year):
    
    if day >= 2:
        day -= 1
    
    elif month >= 2:
        month -= 1
        day = days(month, year)
    
    else:
        year -= 1
        month = 12
        day = days(month, year)

    return day, month, year


def next_date(day, month, year):

    if day < days(month, year):
        day += 1
    
    elif month < 12:
        month += 1
        day = 1
    
    else:
        year += 1
        month = 1
        day = 1

    return day, month, year


values = list()
values = input("День, месяц, год через пробел: ").split()
day = int(values[0])
month = int(values[1])
year = int(values[2])


previous_day = previous_date(day, month, year)
next_day = next_date(day, month, year)

print(f"Предыдущий день: {str(previous_day[0]).zfill(2)}/{str(previous_day[1]).zfill(2)}/{previous_day[2]}")
print(f"Следующий день: {str(next_day[0]).zfill(2)}/{str(next_day[1]).zfill(2)}/{next_day[2]}")

# Удалите комментарий и допишите код

# --------------
# Пример вывода:
#
# День, месяц, год через пробел: 1 3 2000
# Предыдущий день: 29/02/2000
# Следующий день: 02/03/2000
