#!/usr/bin/env python
#_*_ coding: utf8 _*_

def saludo(nombre, edad):
    print("Hola {} tienes: {}".format(nombre, edad))

def main():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    saludo(nombre, edad)

if __name__ == "__main__":
    main()