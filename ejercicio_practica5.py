

""" Ejercicio 5

Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital 
obtenido en la inversión cada año que dura la inversión. """

def capital_obtenido(amount,interest,years):
    '''
    Función que calcula el interés anual
    '''
    
    for i in range(years):
        print('Capital obtenido el '+str(i+1)+'° año ')
        amount+= (amount * interest)    
        print(amount)
        print(' -------------------------------------- ')

if __name__ == '__main__':
    amount = float(input('¿Cantidad a invertir?: '))
    interest = float(input('Ingrese el porcentaje: '))
    years = int(input('Ingrese la cantidad de años: '))

    capital_obtenido(amount, interest, years)