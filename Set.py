# Множества в Python являются структурами данных, которые содержат
# неповторяющиеся элементы. Множества полезны для выполнения таких операций,
# как объединение, пересечение и разность между двумя или более множествами.

# Множество можно создать с помощью фигурных скобок {} или с помощью встроенной функции set().
# Создаем множество с помощью фигурных скобок
# my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
# print(my_set)
# my_type1 = type(my_set)
# print(my_type1)

# Создаем множество с помощью функции set()
my_set1 = set([1, 2, 3, 4, 5])
# print(my_set1)
# my_type = type(my_set1)
# print(my_type)

# Для добавления элемента в множество используется метод add()
# my_set1.add(6)
# print(my_set1)

# Для удаления элемента из множества используются методы remove()
# или discard(). Разница между ними заключается в том, что remove()
# вызовет ошибку, если элемент не найден, а discard() выполнится без ошибок.
# my_set1.remove(1)
# print(my_set1)

# my_set1.discard(2)
# print(my_set1)

# Для объединения множеств используется метод union() или оператор |.
set_a = {1, 2, 3, 4, 5, 8, 9}
set_b = {1, 2, 3, 4, 5}
# union_a = set_a.union(set_b)
# union_b = set_a | set_b
# print(union_a)
# print(union_b)

# Для нахождения пересечения множеств используется метод intersection() или оператор &.
# intersection_a = set_a.intersection(set_b)
# intersection_b = set_a & set_b
# print(intersection_b)
# print(intersection_a)

# Для нахождения разности множеств используется метод difference() или оператор -.
# difference_a = set_a.difference(set_b)
# difference_b = set_a - set_b
# difference_a = set_b - set_a
# print(difference_b)
# print(difference_a)

# Принадлежность элемента множеству
# my_set2 = {'биология', 'химия', 'история'}
# print('математика' in my_set2)
# print('математика' not in my_set2)

# Как и в случае с кортежами, результатом сортировки множества будет список
numbers = {12, 9, 1, 5, 3, 11, 2, 6, 8, 10, 7}
print(numbers)
print(type(numbers))
print(sorted(numbers))
print(sorted(numbers, reverse=True))
for num in numbers:
    print(num)

# Множества можно сравнивать с помощью операторов == и !=:
print(set_a != set_b)
print(set_a == set_b)

# при сравнении множеств Python определяет,
# является ли одно из них под- или надмножеством другого
print(set_a > set_b)

# Несколько элементов можно добавить с помощью цикла for
set_c = set()
gen = {set_c.add(i) for i in range(12)}
print(set_c)

# pop() – в отличие от аналогичного списочного метода,
# удаляет случайный элемент и возвращает его значение
new = set_c.pop()
print(new)
print(set_c)
set_c.add(new)
print(set_c)

set_new = set([1, 2, 2, 5, 5, 3, 4, 3, 4])
print(set_new)
