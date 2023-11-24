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

