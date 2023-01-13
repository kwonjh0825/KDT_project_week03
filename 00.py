import requests

def btc_krw():
    order_currency = 'BTC'
    payment_currency = 'KRW'
    url = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

    res = requests.get(url).json()
    data = res['data']
    prev_closing_price = data['prev_closing_price']

    return prev_closing_price

print(btc_krw())