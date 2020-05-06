""" Ejercicio 4

Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla la cuenta atrás desde ese 
número hasta cero separados por comas. """

def mostrar_numeros(numero):
    
    for i in range(numero, 0, -1):
        print(i)

if __name__ == '__main__':
    
    numero = int(input('Ingrese un número entero: '))
    mostrar_numeros(numero)