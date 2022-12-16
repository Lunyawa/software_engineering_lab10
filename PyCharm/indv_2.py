#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    a = input('\n\nВведите строку ')
    s1 = set(a.replace(' ', ''))

    a = input('Введите строку ')
    s2 = set(a.replace(' ', ''))

    intersec = s1.intersection(s2)
    print('общие символы = ', intersec)
    print('количесвто общих символов = ', len(intersec))