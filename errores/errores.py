#!/usr/bin/env python
#_*_ coding: utf8 _*_

""" try:
    while True:
        print("Hola")
except NameError:
    print("L no esta definido")
except KeyboardInterrupt:
    print("Salida forzosa")
finally:
    print("Terminó la ejecución") """

try:
    raise IOError
except IOError:
    print("Ocurrio un error")