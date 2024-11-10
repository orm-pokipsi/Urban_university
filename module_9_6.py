print('Домашнее задание по теме "Генераторы"')


def all_variants(text: str):
    length = len(text)
    for size in range(1, length + 1):
        for i in range(length - size + 1):
            yield text[i:i + size]

a = all_variants("abc")
for n in a:
    print(n)
