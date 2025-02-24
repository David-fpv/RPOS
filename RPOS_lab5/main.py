import re

def isValidNumberCard (card_number):
    return re.fullmatch("(\d{16})|(\d{4}-\d{4}-\d{4}-\d{4})", card_number)

n = int(input())
card_numbers = list()

for i in range(n):
    card_numbers.append(input())

for i in card_numbers:
    if isValidNumberCard(i):
        print("Valid")
    else:
        print("Invalid")