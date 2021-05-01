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
        print(model)

    def run(self):
        print('run')

class TeslaCar(Car):
    def __init__(self, model = None):
        super().__init__(model)
        print("####")

    def auto_run(self):
        print('auto_run')

tesla_car = TeslaCar("Model S")
tesla_car.run()
tesla_car.auto_run()
