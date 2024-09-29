print('Домашнее задание по уроку "Пространство имен":')
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

inner_function()  # ошибка функции так как мы не можем доставать значения вне функции test_function

test_function()