# Создайте  иерархию  классов  с использованием  множественного  наследования.  Выведите  на экран
# порядок  разрешения  методов  для  каждого  из  классов.  Объясните,  почему  линеаризации  данных
# классов выглядят именно так.


class Cycle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive_forward(self):
        print("Drive forward")

    @staticmethod
    def rules():
        print('You can drive even in childhood')


class Motorcyle(Cycle):
    def __init__(self, brand, color, model):
        Cycle.__init__(self, brand, color)
        self.motorcycle_model = model

    def long_distances(self):
        print('Ability to travel for a long time')

    @staticmethod
    def traffic_jam():
        print('You can move faster in a traffic jam')


class Car(Motorcyle, Cycle,):
    def __init__(self, brand, color, model, type_of_fuel):
        Motorcyle.__init__(self, brand, color, model)
        Cycle.__init__(self, brand, color)
        self.car_type_of_fuel = type_of_fuel

# class Car(Cycle, Motorcyle):
        # def __init__(self, brand, color, model, type_of_fuel):
            # super().__init__(brand, color, model)
            # self.type_of_fuel = type_of_fuel
    def drive_backward(self):
        print('Drive backward')


def main():
    cycle = Cycle(brand='bmc', color='white')
    cycle.drive_forward()
    cycle.rules()
    motorcycle = Motorcyle(brand='yamaha', color='red', model='tenere')
    motorcycle.drive_forward()
    motorcycle.long_distances()
    motorcycle.traffic_jam()
    car = Car(brand='bmw', color='black', model='x3', type_of_fuel='A-95')
    car.drive_forward()
    car.long_distances()
    car.drive_backward()
    print(Car.mro())


if __name__ == '__main__':
    main()