m = [0] * 21
count = 0


def Fib2(N):
    global count
    count += 1

    if m[N] != 0:
        return m[N]

    if N == 1 or N == 2:
        m[N] = 1
    else:
        m[N] = Fib2(N - 2) + Fib2(N - 1)

    return m[N]


for i in range(5):
    n = int(input(f"Введите номер {i + 1} (от 1 до 20): "))
    before = count
    result = Fib2(n)
    use = count - before
    print(f"F({n}) = {result} (вызовов для этого запроса: {use})")
