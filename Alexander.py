# my_tuple = tuple('Привет')
# print(my_tuple)

x = "Строка"
enumerate_x = list(enumerate(x))
print(enumerate_x)
enumerate_y = list(enumerate(x, - 10))
print(enumerate_y)

for item in enumerate_y:
    print(item)
