# Выведите из списка чисел список квадратов четных чисел. Используйте 2 варианта решения: генератор и
# цикл

def rev_gen(my_list):
    for y in my_list:
        if y % 2 == 0:
            yield y ** 2
        else:
            print('нечетное число')


lst = [1, 2, 3, 5, 6, 7, 8, 9, 10]
for i in rev_gen(lst):
    print(i)

# не понимаю в чем здесь ошибка
def generator(my_list):
    for i in my_list:
        yield i**2 if i % 2 == 0 else print('Нечетное число')


gen = generator([1, 2, 3, 5, 6, 7, 8, 9, 10])
for i in gen:
    print(i)


# my_gen = (x ** 2 for x % 2 in my_list)
# print(my_gen)


my_list = [1, 2, 3, 5, 6, 7, 8, 9, 10]
for i in my_list:
    if i % 2 == 0:
        print(i ** 2)
    else:
        print('Нечетное число')