#!/usr/bin/env python
#_*_ coding: utf8 _*_

# Se se usa el modo write se reescribe todo el documento

archivo = open("archivo1.txt", "a")
dedicacion = input("Dedicación: ")
empresa = input("Empresa: ")
idioma = input("Idioma: ")

archivo.write("\n")
archivo.write(dedicacion)
archivo.write("\n")
archivo.write(empresa)
archivo.write("\n")
archivo.write(idioma)

archivo.close()