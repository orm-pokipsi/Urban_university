print('Задача "Нули ничто, отрицание недопустимо!":')
a = 0
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while True:
    if (a < len(my_list) and my_list[a] >= 0):
        if (my_list[a] > 0):
            print(my_list[a])
        a +=1
        continue
    else:
        break
