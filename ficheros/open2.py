#!/usr/bin/env python
#_*_ coding: utf8 _*_

archivo = open("wordlist.lst", "r")

# print(archivo.readlines())

for l in archivo.read().split("\n"):
    print(l)