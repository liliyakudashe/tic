# Список в Python - это упорядоченная изменяемая коллекция объектов,
# которые могут быть различных типов данных. Список создается с помощью квадратных скобок []
# и элементы списка разделяются запятыми.
# Списки могут содержать любое количество элементов и элементы могут быть добавлены,
# удалены или изменены после создания списка. Списки также поддерживают различные методы,
# такие как сортировка, объединение и разделение.

my_list = [1, 'Privet', 3, 'Poka']
# Добавление элемента в список:
# list.append(x) - добавляет элемент x в конец списка.
# list.insert(i, x) - добавляет элемент x на позицию i.
my_list.append('Kak dela')
my_list.insert(2,'Horosho')
print(my_list)
print('*' * 50)

# Удаление элемента из списка:
# list.remove(x) - удаляет первый элемент со значением x.
# list.pop([i]) - удаляет элемент на позиции i, если i не указан, удаляется последний элемент.
my_list.remove('Privet')
print(my_list)
print('*' * 50)
my_list.pop(1)
print(my_list)
print('*' * 50)

# Получение информации о списке:
# len(list) - возвращает количество элементов в списке.
# list.index(x) - возвращает индекс первого элемента со значением x.
# list.count(x) - возвращает количество элементов со значением x.
my_len = len(my_list)
print(my_len)
print('*' * 50)
my_index = my_list.index(3)
print(my_index)
print('*' * 50)
my_count = my_list.count('Privet')
print(my_count)
print('*' * 50)

# Сортировка списка:
# list.sort() - сортирует список по возрастанию.
# list.sort(reverse=True) - сортирует список по убыванию.
list_name = [2, 8, 1, 3, 5, 4, 6, 7]
my_sort = list_name.sort()
print(my_sort)
print('*' * 50)
list_name.sort(reverse=True)
print(list_name)
print('*' * 50)

# Обращение к элементам списка:
# list[i] - возвращает элемент на позиции i.
# list[start:stop:step] - возвращает срез списка от позиции start до stop с шагом step.
my_element = list_name[2]
print(my_element)
print('*' * 50)
l1, l2, l3, l4, l5, l6, l7, l8 = list_name
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print(l6)
print(l7)
print(l8)
lists = my_list + list_name
print(lists)

print('*' * 50)
animals = ['cat', 'dog', 'bat']
for animal in animals:
    print(animal)

i = 0
while i < len(animals):
    print(animals[i])
    i += 1

print('*' * 50)
min_list = min(list_name)
print(min_list)
max_list = max(list_name)
print(max_list)

a = [12, 19, 10, 14, 10]
b = a[0]
print(b)
c = a[3:]
print(c)
# help(list_name)
