def check_password(password):
    if len(password) < 6 or password.isdigit() == True:
        return ('Слабый')
    if len(password) > 6 or password.isdigit() == False:
        return ('Нормальный')


print(check_password("1234567"))
print(check_password("kot2026"))
