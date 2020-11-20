#!/usr/bin/env python
#_*_ coding: utf8 _*_

# classmethod
# staticmethod
# property

class prueba1(object):
    def __init__(self, radio):
        self.radio = radio
    
    @classmethod # Nos ayuda a usar una funcion sin que antes la clase sea atribuida a un objeto
    def saludo(cls, nombre):
        print("Hola {}".format(nombre))
    
    @staticmethod
    def saludo_static():
        print("Bienvenido")
    
    @property
    def area_circulo(self):
        return (self.radio**2) * 3.1416

def main():
    # nombre = input("Nombre: ")
    # prueba1.saludo(nombre)

    # c = prueba1()
    # c.saludo_static()

    c = prueba1(5)
    area = c.area_circulo
    print(area)

if __name__ == "__main__":
    main()