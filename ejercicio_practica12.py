
""" Ejercicio 12

Escribir un programa en el que se pregunte al usuario por una frase 
y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase. """


def mostrar_letra(letra,frase):
    
    contador = 0

    for i in frase:
        
        if letra == i:
            contador+=1
    
    print('La letra {} aparece {} veces en la palabra {} '.format(letra, contador, frase))

if __name__ == '__main__':
    frase = input('Ingrese una palabra: ')
    letra = input('Ingrese una letra: ')

    mostrar_letra(letra,frase)