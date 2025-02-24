
# Выполнил: Тарасенко Д.И.
# Группа: МС-32



# В данной задаче ввод с клавиатуры не нужен.
#
# Используйте значения 'votes', при необходимости измените его для
# проверки правильности решения

votes = [
    2, 3, -1, 2, 5, 1, 1, 4, 1, 1, 1, 3, 1, 3, 5, -1, 5, 2, 5, 5,
    3, 3, 2, 3, 3, 2, 2, 1, 3, 2, 5, 2, 2, 4, 1, 1, 3, 2, 2, 3, 3,
    3, 1, 4, 2, 1, 4, 2, 3, 3, 3, -1, 5, 3, 1, 4, 5, 1, 1, 3, 3,
    3, -1, 5, 3, 3, 2, 5, 1, 1, 5, -1, 1, 2, 2, 3, -1, 4, 2, 5, 4,
    2, -1, 3, 1, 4, 3, 5, 4, 1, 5, 3, 2, 4, 2, 1, 3, 4, 1, 1, 3, 4
]

parties = {
    1: "Партия №1", 2: "Партия №2", 3: "Партия №3",
    4: "Партия №4", 5: "Партия №5", -1: "Испорчено"
}


def parties_votes(parties, votes):
    parties_votes_result = dict()

    for key, value in parties.items():
        parties_votes_result[value] = 0

    for i in votes:
        for key, value in parties.items():
            if i == key:
                parties_votes_result[value] += 1
                break

    return parties_votes_result


def print_results(votes_for_p):
    count_votes = 0
    for key, value in votes_for_p.items():
        count_votes += value

    sorted_votes_for_p = dict(sorted(votes_for_p.items(), key=lambda item: item[1], reverse=True))
    
    position = 1
    for key, value in sorted_votes_for_p.items():
        print("{:1}. {:9} | {:2} | {:2.2f}%".format(position, key, value, value/count_votes*100))
        position += 1


print_results(parties_votes(parties, votes))

# --------------
# Пример вывода:
#
# 1. Партия №3 | 27 | 26.47%
# 2. Партия №1 | 22 | 21.57%
# 3. Партия №2 | 20 | 19.61%
# 4. Партия №5 | 14 | 13.73%
# 5. Партия №4 | 12 | 11.76%
# 6. Испорчено |  7 |  6.86%
