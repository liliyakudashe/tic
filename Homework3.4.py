def test(*args):
    for arg in args:
        print(arg)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

test('Гарри', 'Поттер')
print(factorial(12))