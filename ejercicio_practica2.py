""" Ejercicio 2

Escribir un programa que pregunte al usuario su edad 
y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad). """


def mostrar_edad(edad_usuario):
    
    for i in range(1,edad_usuario+1):
        print('Ha cumplido '+str(i))

if __name__ == '__main__':
    edad_usuario = int(input('Ingrese su edad: '))
    mostrar_edad(edad_usuario)