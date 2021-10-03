# Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение,
# если пользователь введёт определённое значение, и перехватите это исключение при вызове функции.

class MyClassException(Exception):
    def func(self):
        try:
            a = input('введите позитивное число: ')
            a = float(a) > 0
        except ValueError:
            print("Uncorrect value")
        except TypeError:
            print("Some value was incorrect!")
        else:
            print('вы ввели', a)
        finally:
            print('Конец программы')


mycls = MyClassException()
mycls.func()