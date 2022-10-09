#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':

    # x = (a - b) & (c | d)
    # y = (a & not_b) | (c - d)

    a = set("bdlp")
    b = set("bdelpx")
    c = set("klpt")
    d = set("dkopquv")
    u = set("abcdefghijklmnopqrstuvwxyz")

    not_b = u.difference(b)
    x = (a.difference(b)).intersection(c.union(d))
    y = (a.intersection(not_b)).union(c.difference(d))

    print("X = ", x)
    print("Y = ", y)
