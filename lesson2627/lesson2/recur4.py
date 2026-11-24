count = 0


def fib1(n):
    global count
    count += 1

    if n == 1 or n == 2:
        return 1

    return fib1(n - 2) + fib1(n - 1)


for i in range(5):
    k = int(input("Введите номер: "))
    count = 0

    result = fib1(k)

    print("Число Фибоначчи:", result)
    print("Количество вызовов:", count)
