

def validate(arrays, mensaje):
    arrays = list(map(lambda x : x.upper(), arrays))
    currency = input(mensaje).upper()
    while currency not in arrays:
        print('La criptomoneda permitida es', arrays)
        currency = input(mensaje)
    return currency

def output(status, cripto, fiat, data):
    if status :
        print(f'1 {cripto} vale {data:.2f} {fiat}')
    else :
        print(f'Se ha producido el error: {data}')