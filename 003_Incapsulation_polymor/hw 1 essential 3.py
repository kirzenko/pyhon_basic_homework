# Организуйте архитектуру приложения “База данных” (псевдо). В роли базы данных у вас
# будет класс  Database, который будет хранить данные в виде переменной списка.
# 2. Класс Database должен иметь методы read_data(criteria),  write_data(element).
# 3. Для элемента данных напишите класс Data. В данном случае мы будем хранить данные о
# пользователях. Data будет иметь атрибуты: country, name, age, gender, height, weight.
# 4. В классе Database метод read_data будет принимать на вход аргумент criteria, который
# является  словарем  вида  {“age”:  25},  после  чего  метод  вернет  отдельный  список  всех
# элементов у которых данное условие истино.
# Подсказка: чтобы получить у объекта класса значение его атрибута как у словаря, используйте
# следующий синтаксис: your_class_instance.__dict__.get(‘name’).
# PS: организуйте правильную инкапсуляцию. Вы должны добавлять элементы в класс Database
# только через метод write, но никак не напрямую через атрибут elements.


class Data:
    def __init__(self, country, name, age, gender, height, weight):
        self.country = country
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight


class Database(Data):
    def __init__(self, country, name, age, gender, height, weight):
        Data.__init__(self, country, name, age, gender, height, weight)

    def read_data(self, criteria):
        #self.criteria = criteria
        pass
    def write_data(self, element):
        #self.element = element
        pass


def main():
    pass


if __name__ == "__main__":
    main()




