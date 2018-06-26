import requests

#sergio fonseca
#23-06-2018
r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
numero = r.json()['bpi']['USD']['rate_float']

print('Cotação do Bitcoin em Dolar: ${0}' .format(numero))


