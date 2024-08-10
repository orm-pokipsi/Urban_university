# все ли равны?
first = int(input('Введите число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first / second == 1 and first / third == 1 and second / third == 1:
    print('3')# если совпали 3 введенных числа
elif first / second == 1 or first / third == 1 or second / third == 1:
    print('2')# если совпали 2 введенных числа
else:
    print('0')# если ни одно число не совпало