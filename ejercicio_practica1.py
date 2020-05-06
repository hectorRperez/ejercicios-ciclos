""" Ejercicio 1

Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces. """

def mostrar_palabra(palabra):
    
    for i in range(10):
        print(palabra)


if __name__ == '__main__':
    
    palabra = input('Ingrese una palabra: ')
    mostrar_palabra(palabra)