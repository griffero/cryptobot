import urllib2, json, datetime

url_btc = "https://api.gdax.com/products/BTC-USD/ticker"
url_eth = "https://api.gdax.com/products/ETH-USD/ticker"
currencies_path = "/root/cryptobot/currencies/"

# Datos BTC-USD
# {"trade_id":22347035,"price":"6075.10000000","size":"0.00000164","bid":"6075.09","ask":"6075.1","volume":"14869.12869290","time":"2017-10-21T22:24:12.177000Z"}
response = urllib2.urlopen(url_btc, timeout=2.5)
data = json.loads(response.read())

btc_usd = {}

btc_usd['market_name'] = 'GDAX'
btc_usd['currencies'] = 'BTC-USD'
btc_usd['last_price'] = float(data['price'])
btc_usd['min_ask'] = float(data['ask'])
btc_usd['max_bid'] = float(data['bid'])
btc_usd['last_update'] = str(datetime.datetime.now()).split('.')[0]



with open(currencies_path + 'gdax_btc_usd.json', 'w') as outfile:
    json.dump(btc_usd, outfile)

print btc_usd


#print data

# Datos BTC-ETH
# Output: {"high": "4865.00", "last": "4805.04", "timestamp": "1507604582", "bid": "4800.17", "vwap": "4691.78", "volume": "13243.35500195", "low": "4541.00", "ask": "4805.03", "open": "4761.67"}

eth_usd = {}

response = urllib2.urlopen(url_eth, timeout=2.5)
data = json.loads(response.read())

eth_usd['market_name'] = 'GDAX'
eth_usd['currencies'] = 'ETH-USD'
eth_usd['last_price'] = float(data['price'])
eth_usd['min_ask'] = float(data['ask'])
eth_usd['max_bid'] = float(data['bid'])
eth_usd['last_update'] = str(datetime.datetime.now()).split('.')[0]



with open(currencies_path + 'gdax_eth_usd.json', 'w') as outfile:
    json.dump(eth_usd, outfile)

print eth_usd
