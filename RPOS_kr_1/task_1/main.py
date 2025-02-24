def numeric_triangle (n):
    for i in range(1,n):
        print(i * (10**i - 1) // 9)

numeric_triangle(int(input()))