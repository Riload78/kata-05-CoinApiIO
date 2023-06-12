import requests

apikey = 'E05C549F-3ED7-47E6-A214-844E08FEA832'

url = f'https://rest.coinapi.io/v1/exchangerate/BTC/USD?apikey={apikey}'

response = requests.get(url)

print(response.status_code)
print(response.text)