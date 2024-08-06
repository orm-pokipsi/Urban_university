immutable_var = 'oppo','xiaomi','apple','samsung'
print("Immutable tuple:",(immutable_var))
#immutable_var.remove ('oppo') #если мы захотим изменить этот элемент, попросим вывести кортеж на экран, то столкнемся с ошибкой
mutable_list = ['oppo','xiaomi','apple','samsung']
mutable_list.extend(['realmi'])
print("Mutable list:",(mutable_list))
