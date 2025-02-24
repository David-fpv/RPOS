def triangle(n):
    for i in range(1, n+1):
        print((123456789 // (10**(9-i))) * (10**(i-1)) + 987654321 % (10**(i-1)))

triangle(5)