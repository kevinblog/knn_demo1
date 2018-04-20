class Car:
    price = 100000  # 定义类属性

    def __init__(self, c):
        self.color = c  # 定义实例属性


car1 = Car("Red")
car2 = Car("Blue")
print(car1.color, Car.price)

Car.price = 110000  # 修改类属性
Car.name = 'QQ'  # 增加类属性
car1.color = "Yellow"  # 修改实例属性
print(car2.color, Car.price, Car.name)
print(car1.color, Car.price, Car.name)

print('------------私有成员方法的使用------------')


class A:
    def __init__(self, value1=0, value2=0):
        self._value1 = value1
        self.__value2 = value2

    def setValue(self, value1, value2):
        self._value1 = value1
        self.__value2 = value2

    def show(self):
        print(self._value1)
        print(self.__value2)


a = A()
print(a._value1)
print(a._A__value2)  # 在外部访问对象的私有数据成员
