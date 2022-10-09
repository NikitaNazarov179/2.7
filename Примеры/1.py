#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    # Генерация множества a с циклом for для несокльких чисел
    a = {i for i in [1, 2, 0, 1, 3, 2]}
    print(a)

    # Получение размера множества
    print(len(a))

    # Добавление элемента
    a.add(4)
    print(a)

    # Удаление элемента
    a.remove(4)
    print("remove", a)
    a.discard(5)
    print("discard: ", a)
    a.pop()
    print("pop", a)

    # Очистка множества
    a.clear()
    print(a)

    # Элементы разных типов данных в одном множестве
    b = {0, 1, 12, 'b', 'ab', 3, 2, 'a'}
    print(b)

    # Если в множестве только числа, они будут отсортированы по возрастанию
    b = {0, 1, 12, 3, 2}
    print(b)

    b = {0, 1, 12, 3, 2}
    c = list(b)
    print(c)

    # Объедимнение множеств
    a = {0, 1, 2, 3}
    b = {4, 3, 2, 1}
    c = a.union(b)
    print(c)

    # Добавление
    a.update(b)
    print(a)

    # пересечение множеств
    a = {0, 1, 2, 3}
    b = {4, 3, 2, 1}
    c = a.intersection(b)
    print(c)

    # Рахность множеств
    a = {0, 1, 2, 3}
    b = {4, 3, 2, 1}
    c = a.difference(b)
    print(c)

    # Подмножество
    a = {1, 2, 3, 4}
    b = {3, 2, 1}
    print(a.issubset(b))

    # Надмножество
    print(a.issuperset(b))

    # Тип frozenset
    g = {"hello", "world"}
    g = frozenset(g)
    print(g, "\n")

    # Преобразование множеств в строку
    a = {'set', 'str', 'dict', 'list'}
    b = ' - '.join(a)
    print(b)
    print(type(b), "\n")

    # В словарь
    e = {('a', 2), ('b', 4)}
    f = dict(e)
    print(f)
    print(type(f), "\n")

    # В список
    a = {1, 2, 0, 1, 3, 2}
    b = list(a)
    print(b)
    print(type(b))