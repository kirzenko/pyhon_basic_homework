# Напишите генератор, который возвращает элементы заданного списка в обратном порядке (аналог
# reversed).

def rev_gen(my_list):
    for i in reversed(my_list):
        yield i


for i in rev_gen([1, 2, 3, 4, 5]):
    print(i)



