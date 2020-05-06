""" Ejercicio 7

Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10. """

def mostrar_tabla_multiplicar():
    
    for i in range(1,11):
        for j in range(1,11):
            print(i*j, end = ' ')

        print(' ')

if __name__ == '__main__':
    mostrar_tabla_multiplicar()