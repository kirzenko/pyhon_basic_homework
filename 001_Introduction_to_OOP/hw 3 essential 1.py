# Создайте класс Tiger, унаследованный от класса Cat (созданного во время практической части занятия).
# Переопределите метод set_size таким образом, чтобы если self.cat_type это ‘wild’, то self.size
# = ‘big’, иначе self.size=’undefined’.

class Cat:
    def __init__(self, color, cat_type, size="undefined"):
       self.size = size
       self.color = color
       self.cat_type = cat_type

    def set_size(self):
        if self.cat_type == 'indoor':
            self.size = 'small'
        elif self.cat.type == 'wild':
             self.size = 'big'
        else:
            self.size = 'undefined'


class Tiger(Cat):
    def __init__(self, color, cat_type, size):
        Cat.__init__(self, color, cat_type, size="undefined")

    def set_size(self):
        if self.cat_type == 'wild':
            self.size = 'big'


def main():
    barsik = Cat('black', 'indoor')
    print('Cat type: ', barsik.cat_type)
    barsik.set_size()
    print('Cat size: ', barsik.size)

    tiger = Tiger('brown, black and white', 'wild', 'big')
    print('Cat type: ', tiger.cat_type)
    tiger.set_size()
    print('Tiger size: ', tiger.size)


if __name__ == '__main__':
    main()








