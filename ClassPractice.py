class Person(object):

    def __init__(self, name = 'Jun'):
      self.name = name
      print(name)

    def say_something(self):
        print('I am {}. Hello.'.format(self.name))
        self.run(5)

    def run(self, num):
        print('run' * num)

person = Person('Mike')
person.say_something()


# 継承
class Car:
    def __init__(self, model = None):
        self.model = model

    def run(self):
        print('run')

class TeslaCar(Car):
    def __init__(self, model = None,
                 enable_auto_run = False,
                 password = 123) :
        super().__init__(model)
        print("####")
        self.__enable_auto_run = enable_auto_run
        self.password = password

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.password == 123:
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print("アンスコ2", self.__enable_auto_run)


tesla_car = TeslaCar("Model S", password = 123)
tesla_car.run()
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)
print(tesla_car.model)
