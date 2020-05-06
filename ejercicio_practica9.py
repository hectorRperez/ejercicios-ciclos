""" Ejercicio 9

Escribir un programa que almacene la cadena de caracteres contraseña en 
una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


Modulo getpass

from getpass import getpass """

from getpass import getpass

def mostrar_contrasena():
    password = 'contraseña'

    while True:
        
        password1 = getpass('Ingrese la contraseña correcta: ')

        if password == password1:
            print('Contraseña correcta')
            break
        else:
            print('Contraseña incorrecta')

if __name__ == '__main__':
    mostrar_contrasena()