# Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание,
# умножение, деление и возведение в степень. Программа должна выдавать сообщения об ошибке и
# продолжать  работу  при  вводе  некорректных  данных,  делении  на  ноль  и  возведении  нуля  в
# отрицательную степень.


a = float(input('введите а: '))
b = float(input('введите b: '))
choice = input('''
                     Выберите необходимую операцию:
                     1. sum
                     2. sub
                     3. mult
                     4. div
                     5. pow
                        ''')


try:
    if choice == '1':
        print(f'a + b = : {a + b}')

    elif choice == '2':
        print(f'a - b = : {a - b}')

    elif choice == '3':
        print(f'a * b = : {a * b}')

    elif choice == '4':
        print(f'a / b = : {a / b}')

    elif choice == '5':
        print(f'a ^ b = : {pow(a, b)}')


except ZeroDivisionError:
    print("You can't divide by zero")

except ValueError:
    print("Uncorrect value")