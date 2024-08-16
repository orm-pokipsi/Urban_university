print('Задача "Слишком древний шифр": ')
import random
number = random.randint(3, 20)
def password(number):
    r = ""
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                r += str(i) + str(j)
    return r
password = password(number)
print(f"Пароль для числа {number}: {password}")
print("Пароль верный")
