def fact(n, d):
    if d * d > n:
        if n > 1:
            print(n, " ")
        return

    if n % d == 0:
        print(d, " ")
        fact(n / d, d)
    else:
        fact(n, d + 1)


n = int(input("Введите число которое хотите разложить на простые множители : "))
fact(n, 2)
