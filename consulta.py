import requests

apikey = 'E05C549F-3ED7-47E6-A214-844E08FEA832'

criptos = ['BTC', 'ETC', 'USDT', 'BNB', 'USDC']
fiats = ['EUR', 'USD', 'JPY']

def validate(arrays, mensaje):

    currency = input(mensaje)
    while currency not in arrays:
        print('La criptomoneda permitida es', arrays)
        currency = input(mensaje)
    return currency
        
cripto = validate(criptos, '¿Que moneda quieres?')
fiat = validate(fiats, '¿En que moneda quieres?')

def  get_rate(cripto, fiat):
    url = f'https://rest.coinapi.io/v1/exchangerate/{cripto}/{fiat}?apikey={apikey}'
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return  True, data['rate']
            
        else:
             return  False, data['error']
    except requests.exceptions.RequestException as e:  #Excepciopnes del requests -> documentación
        return str(e)
    
status, data = get_rate(cripto, fiat)

if status :
    print(f'1 {cripto} vale {data:.2f} {fiat}')
else :
    print(f'Se ha producido el error: {data}')
