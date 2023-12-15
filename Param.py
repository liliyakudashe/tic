def unpacking(param1=1, param2=2, param3=3):
    print(param1, param2, param3)

unpacking()
unpacking(4)
unpacking(4, 5)
unpacking(4, 5, 6)

def unpacking_str(param1='A', param2='B', pfram3='C'):
    print(param1, param2, pfram3)

unpacking_str()
unpacking_str('T')
unpacking_str('T', 'N')
unpacking_str('T', 'N', 'D')

def numbers(a, b, c):
    print(a, b, c)

int_list = [4, 5, 6]
res = numbers(*int_list)

def test(a, b, c):
    return (a ** 2 + b ** + 2 + c ** + 2) ** 5

# распаковка позиционных параметров
sone_list = [1, 2, 3]
res1 = test(*sone_list)
print(res1)

# распаковка именных параметров
sone_dict = {'a': 1, 'b': 2, 'c': 3}
res = test(**sone_dict)
print(res)

def test():
    a = 10
    b = 12
    print(a)
    print(b)
    print(a + b)


def test2(param1, param2, param3):
    print(param1)
    print(param2)
    print(param3)

test()
test2(2, 3, 4)
test2('Test', 'Test', 'Test')

def process_data(data):
    match data:
        case []:
            print("Нет данных")
        case [x]:
            print(f"Единственный элемент: {x}")
        case [x, y]:
            print(f"Первый элемент: {x}, второй элемент: {y}")
        case _:
            print("Слишком много данных")