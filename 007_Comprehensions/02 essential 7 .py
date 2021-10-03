# Напишите comprehension, который итерирует строку “1_2,40_5,5_32” (разбить по запятым)
# и каждый элемент разбивает по символу “_” и полученные элементы приводит к типу int,
# и складывает их, тем самым образуя список целых чисел. (Вы можете использовать lambda
# функцию или написать обычную, которая принимает строку вида “1_2” на вход и
# возвращает число как сумму значений из строки; используйте метод split())

# а как их теперь просуммировать?
#numbers = '1_2,40_5,5_32'
#numbers_1 = numbers.split(',')
#numbers_2 = [i.split('_') for [i] in numbers_1]
# result = [int(elem) for elem in numbers_2]
#print(numbers_2)
a = '1_2,40_5,5_32'
c = [int(num.split('_')[0]) + int(num.split('_')[1]) for num in a.split(',')]
print(c)



#numbers_2 = [i.split('_')[0] + i.split('_')[1] + i.split('_')[2] + i.split('_')[3] for i in numbers_1]
#int_numbers = [int(i) for i in numbers_2] # не получается перевести в int
#print(int_numbers)
