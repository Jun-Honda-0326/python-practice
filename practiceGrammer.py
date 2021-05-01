
# デコレータif文
print('if文')

x = 10
if x < 0:
    print('negative')
elif x == 0:
  print('zero')
else:
    print('positive')

a = 5
b = 10
if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positice')

y = [1, 2, 3]
x = 1
if x in y:
    print('in')
if 100 not in y:
    print('not in')

print('----------')

# while文
print('while文')

count = 0
while True:
    if count >= 5:
        break
    if count == 2:
        count += 1
        continue
    print(count)
    count += 1

print('while else')
count_2  = 0
while count_2 < 5:
    print(count_2)
    count_2 += 1
else:
    print('done')

print('----------------')

# for文
print('for文')

num_list = [1, 2, 3, 4, 5]
for i in num_list:
    print(i)

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    if fruit == 'orange':
        print('stop eating')
        break
    print(i, fruit)
else:
    print('I ate all!')

for i in (range(2, 8, 3)):
    print(i, 'hello')

days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)


d = {'x': 100, 'y': 200}
print(d.items())
for k, v in d.items():
    print(k, ':',  v)

# 関数定義
def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green papper'
    else:
        return "I don't know"
result = what_is_this('green')
print(result)

def say_something(word, *args):
    print('word = ', word )
    for arg in args:
        print(arg)
say_something('Hi', 'Mike', 'Michel')

def menu(food, **kargs):
    print('food = ', food)
    for k, v in kargs.items():
        print(k, v)
d = {
  'entree': 'vegitable',
  'drink': 'coffee',
  'desert': 'ice'
}
menu('beef', **d)


# クロージャー
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area
cal1 = circle_area_func(3.14) # return circle_area
print(cal1(10))

# デコレータ
def print_info(func):
    def wrapper(*args, **kwards):
        print('start')
        print(*args)
        result = func(*args, **kwards)
        print('end')
        return result
    return wrapper

@print_info
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

# ラムダ
print('ラムダ')
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri']
def change_words(words, func):
    for word in words:
        print(func(word))
change_words(l, lambda word: word.capitalize())

# ジェネレーター
print('ジェネレーター')
greet = ['Morning', 'Afternoon', 'Night']
def greeting():
    yield 'Morning'
    yield 'Afternonn'
    yield 'Night'

def run(n = 10):
    for _ in range(n):
        yield 'run'
r = run()
g = greeting()

print(next(g))
print(next(r))
print(next(r))
print(next(r))
print(next(g))
print(next(g))
print(next(r))
