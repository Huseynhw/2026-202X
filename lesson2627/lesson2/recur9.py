def nod(a, b):
    if b == 0:
        return a
    return nod(b, a % b)


a = int(input("Введите A: "))
b = int(input("Введите B: "))
c = int(input("Введите C: "))
d = int(input("Введите D: "))

print(f"НОД(A, B) = {nod(a, b)}")
print(f"НОД(A, C) = {nod(a, c)}")
print(f"НОД(A, D) = {nod(a, d)}")
