# Реализуйте цикл, который будет перебирать все значения итерабельного объекта iterable


iterable = ['Реализуйте', 'цикл', ',', 'который', 'будет', 'перебирать', 'все', 'значения', 'итерабельного', 'объекта', 'iterable']

my_iter = iter(iterable)

for element in iterable:
    print(element, end=' ')
    print()