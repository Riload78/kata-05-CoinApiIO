
import requests
apikey = 'E05C549F-3ED7-47E6-A214-844E08FEA832'
criptos = ['BTC', 'ETC', 'USDT', 'BNB', 'USDC']
fiats = ['EUR', 'USD', 'JPY']

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
    