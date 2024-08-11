# все ли равны?
first = int(input('Введите число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second  and first == third and second == third:
    print('3')# если совпали 3 введенных числа
elif first == second or first == third or second == third:
    print('2')# если совпали 2 введенных числа
else:
    print('0')# если ни одно число не совпало
