""" Ejercicio 13

Escribir un programa que muestre el eco de todo lo que el usuario 
introduzca hasta que el usuario escriba “salir” que terminará. """


def mostrar_eco():
    
    while True:

        eco = input('Ingresar una palabra: ')

        if eco == 'salir':
            print('Saliendo...')
            break
        else:
            print(eco)

if __name__ == '__main__':
    mostrar_eco()