#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    str_in = input("Введите строку: ").lower()
    a = set(str_in)
    u = set("аоуыэеёиюяиaeiouy")

    count = 0
    for i in str_in:
        if i in u:
            count = count+1

    print(count)