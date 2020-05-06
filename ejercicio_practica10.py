""" Ejercicio 10

Escribir un programa que pida al usuario un número entero 
y muestre por pantalla si es un número primo o no. """


def mostrar_numero_primo(numero):
    
    if numero % 2 != 0:
        print('El numero {} es primo '.format(numero))

if __name__ == '__main__':

    numero = int(input('Ingrese un número entero: '))
    mostrar_numero_primo(numero)