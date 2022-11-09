import random
import datetime

date = datetime.datetime.now()

def multiply(el):
    return el * 2

my_list = [1,2,3,4]

new_list = list(map(multiply, my_list))
better_list = list(map(lambda *el: el*3, [1,2,3,4,5]))

print(new_list)

print(better_list)
print(random.randint(0, 10))
print(random.random())

print(date)
