import math

def loose_change(cents):
    # Inicializar el diccionario con todas las monedas en 0
    coins = {'Quarters': 0, 'Dimes': 0, 'Nickels': 0, 'Pennies': 0}
    
    # Si es menor o igual a cero, devolvemos el diccionario vacío
    if cents <= 0:
        return coins
        
    # Redondear hacia abajo en caso de recibir un float
    cents = math.floor(cents)
    
    # Calcular la cantidad de monedas de mayor a menor valor
    coins['Quarters'] = cents // 25
    cents %= 25
    
    coins['Dimes'] = cents // 10
    cents %= 10
    
    coins['Nickels'] = cents // 5
    cents %= 5
    
    coins['Pennies'] = cents
    
    return coins