""" Ejercicio 6

Escribir un programa que pida al usuario un número entero y
muestre por pantalla un triángulo rectángulo como el de más abajo, 
de altura el número introducido.

*
**
***
****
***** 

"""


def mostrar_trinagulo(numero):
    
    for i in range(numero):
        for j in range(i):
            print('*',end = '')
        
        print(' ')

if __name__ == '__main__':
    numero = int(input('Ingrese un número entero: '))
    mostrar_trinagulo(numero)