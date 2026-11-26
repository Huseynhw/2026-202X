def root_k(x, k, n):
    if n == 0:
        return 1
    prev = root_k(x, k, n - 1)
    return prev - (prev - x / (prev ** (k - 1))) / k


x = float(input("Введите X (> 0): "))
k = int(input("Введите K (> 1): "))
n_values = [int(input(f"Введите N{i + 1}: ")) for i in range(6)]

for n in n_values:
    print(f"N = {n}: {root_k(x, k, n)}")