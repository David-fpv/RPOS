
# Выполнил: Тарасенко Д.И.
# Группа: МС-32



# В данной задаче ввод с клавиатуры не нужен.
#
# Используйте пример данных ниже, при необходимости измените его для
# проверки правильности решения

data = [
    {1: 'м', 2: 'м', 3: 'м', 4: 'ж'},
    {1: 'ж', 2: 'м', 3: 'ж', 4: 'ж'},
    {1: 'ж', 2: 'ж', 3: 'ж', 4: 'ж'},
    {1: 'м', 2: 'м', 3: 'м', 4: 'м'},
    {1: None, 2: None, 3: None, 4: None},
    {1: 'м', 2: None, 3: None, 4: 'ж'},
    {1: None, 2: None, 3: None, 4: None},
    {1: 'м', 2: 'м', 3: None, 4: 'м'},
    {1: 'ж', 2: None, 3: None, 4: 'ж'}
]


def vacant_compartments(data):
    
    empty_compartment = list()

    for i in range(len(data)):
        for key, value in data[i].items():
            if data[i][key] != None:
                break
        else:
            empty_compartment.append(i+1)

    return empty_compartment


def vacant_seats(data, compartments_condition=None, seat_condition=None):

    vacant_seats_list = list()

    for compartment in range(len(data)):
        for key, value in data[compartment].items():
            if value != None:
                continue
            
            if compartments_condition != None:
                if not compartments_condition(data[compartment]):
                    continue

            if seat_condition != None:
                if not seat_condition(key, value):
                    continue

            vacant_seats_list.append((compartment+1, key))

    return vacant_seats_list


def is_same_sex_and_vacant(compartment, sex):
    vacant_seats = 0
    for key, value in compartment.items():
        if value == None:
            vacant_seats += 1
        elif value != sex:
            return False

    if vacant_seats > 0 and vacant_seats < 4:
        return True


print(vacant_compartments(data))
# список полностью свободных купе
# Удалите комментарий и допишите код
# список свободных мест в вагоне
print(vacant_seats(data))
# список свободных нижних мест
print(vacant_seats(data, seat_condition=lambda seat, value: seat % 2 != 0))
print(vacant_seats(data, seat_condition=lambda seat, value: seat % 2 != 1))
# список свободных верхних мест
# Удалите комментарий и допишите код
# список свободных мест в купе с исключительно мужской компанией
print(vacant_seats(data, lambda x: is_same_sex_and_vacant(x, "м")))
print(vacant_seats(data, lambda x: is_same_sex_and_vacant(x, "ж")))
# список свободных мест в купе с исключительно женской компанией
# Удалите комментарий и допишите код


# --------------
# Пример вывода:
#
# [5, 7]
# [(5, 1), (5, 2), (5, 3), (5, 4), (6, 2), (6, 3), (7, 1), (7, 2), (7, 3),
#  (7, 4), (8, 3), (9, 2), (9, 3)]
# [(5, 1), (5, 3), (6, 3), (7, 1), (7, 3), (8, 3), (9, 3)]
# [(5, 2), (5, 4), (6, 2), (7, 2), (7, 4), (9, 2)]
# [(8, 3)]
# [(9, 2), (9, 3)]
