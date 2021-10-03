# Взяв за основу код примера example_5.py, расширьте функциональность класса MyList, добавив методы
# для очистки списка, добавления элемента в произвольное место списка, удаления элемента из конца и
# произвольного места списка.


"""
Пример реализации списка с итератором
"""


class MyList(object):
    """Класс списка"""

    class _ListNode(object):
        """Внутренний класс элемента списка"""

        # По умолчанию атрибуты-данные хранятся в словаре __dict__.
        # Если возможность динамически добавлять новые атрибуты
        # не требуется, можно заранее их описать, что более
        # эффективно с точки зрения памяти и быстродействия.
        # Специальный классовый атрибут __slots__ позволяет ограничить
        # набор атрибутов, которыми будет обладать экземпляр класса.
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return f'MyList._ListNode({self.value}, {id(self.prev)}, {id(self.next)})'

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head
            self._is_empty = False

        def __iter__(self):
            return self

        def __next__(self):
            if self._is_empty:
                raise StopIteration

            if self._next_node is None:
                self._is_empty = True
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    # *args позволяет передать неограниченное количество параметров,
    # которые далее будут доступны в последовательности по
    # идентификатору args (если параметров нет - она равна False)
    def __init__(self, *args):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None

        # Добавление всех переданных элементов
        if args:
            for element in args:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам последовательности.
        return '[{}]'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        # Проверка, является ли указанный индекс числом
        if isinstance(index, int):
            # Наш список не поддерживает индексацию с конца
            if not 0 <= index < len(self):
                raise IndexError('list index out of range')

            # Сначала выбираем самый первый элемент списка
            node = self._head
            # Затем выбираем следующий элемент списка до тех пор,
            # пока не достигнем нужного по порядку:
            for _ in range(index):
                node = node.next

            return node.value

        # Проверка, является ли указанный индекс срезом
        elif isinstance(index, slice):
            # Запрещено указывать нулевой шаг среза
            if index.step == 0:
                raise ValueError('slice step cannot be zero')

            # Наш список не поддерживает индексацию с конца
            for element in (index.stop, index.start, index.step):
                if element is not None and element < 0:
                    raise IndexError('list index out of range')

            # Создаем срез такого же типа данных, как наш список
            slice_result = MyList()
            # Заменяем значения None для создания диапазона индексов
            for i in range(index.start or 0, index.stop or len(self), index.step or 1):
                # Рекурсивно добавляем в срез элементы согласно их индексу
                slice_result.append(self.__getitem__(i))
            return slice_result
        # Если в качестве индекса указаны другие значения, кроме целых чисел или
        # среза, выбрасываем TypeError с указанием недопустимого типа данных
        else:
            raise TypeError(f'list index cannot be {type(index).__name__}')

    def __iter__(self):
        return MyList._Iterator(self)

    # очистка списка
    def clean_list(self):
        MyList.clear()
        return 'Method for cleaning', MyList

    # добавление элемента
    def append_1(self, element):
        node = MyList._ListNode(element)
        if self._tail is None:
            self._head = self._tail = node
        self._length += 1


def main():
    # Создание списка
    my_list = MyList(1, 2, 3)

    # Вывод длины списка
    print('List length is:', len(my_list))

    # Вывод списка
    print('My list is:', my_list)

    print()

    print('List contains:')

    # Обход списка
    for element in my_list:
        print(element, end=' ')

    print('\nList contains:')

    # Повторный обход списка
    for element in my_list:
        print(element, end=' ')

    # Создание итератора
    my_list_iter = iter(my_list)

    print()
    print('Iterator contains:')

    # Обход итератора
    for element in my_list_iter:
        print(element, end=' ')

    print()

    print('Iterator contains:')

    # Повторный обход итератора (неудача)
    for element in my_list_iter:
        print(element, end=' ')

    print()

    # Вывод элемента списка по индексу
    print(f'my_list[0] = {my_list[0]}, my_list[1] = {my_list[1]}, my_list[2] = {my_list[2]}')

    # Вывод среза элементов списка
    print(f'my_list[1:] = {my_list[1:]}')

    # Тестирование индексирования и срезов
    try:
        print(my_list[-1])
    except IndexError as e:
        print(e)

    try:
        print(my_list[1::-1])
    except IndexError as e:
        print(e)

    try:
        print(my_list[1:2:0])
    except ValueError as e:
        print(e)

    try:
        print(my_list['hello'])
    except TypeError as e:
        print(e)

    print()

    my_list.clean_list()


if __name__ == '__main__':
    main()

