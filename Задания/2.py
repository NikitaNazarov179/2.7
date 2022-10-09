#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':

    str_1 = input("Введите первую строку: ")
    str_2 = input("Введите вторую строку: ")

    mn_1 = set(str_1)
    mn_2 = set(str_2)


    common = mn_1.intersection(mn_2)
    print("Общие символы:", common)