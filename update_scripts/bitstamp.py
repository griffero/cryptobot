import urllib, json, datetime

url_btc = "https://www.bitstamp.net/api/v2/ticker/btcusd/"
url_eth = "https://www.bitstamp.net/api/v2/ticker/ethusd/"

currencies_path = "/root/cryptobot/currencies/"

# Datos BTC-CLP
# Output: {"high": "4865.00", "last": "4805.04", "timestamp": "1507604582", "bid": "4800.17", "vwap": "4691.78", "volume": "13243.35500195", "low": "4541.00", "ask": "4805.03", "open": "4761.67"}
response = urllib.urlopen(url_btc)
data = json.loads(response.read())

btc_usd = {}

btc_usd['market_name'] = 'Bitstamp'
btc_usd['currencies'] = 'BTC-USD'
btc_usd['last_price'] = float(data['last'])
btc_usd['min_ask'] = float(data['ask'])
btc_usd['max_bid'] = float(data['bid'])
btc_usd['last_update'] = str(datetime.datetime.now()).split('.')[0]




with open(currencies_path + 'bitstamp_btc_usd.json', 'w') as outfile:
    json.dump(btc_usd, outfile)

print btc_usd


#print data

# Datos BTC-ETH
# Output: {"high": "4865.00", "last": "4805.04", "timestamp": "1507604582", "bid": "4800.17", "vwap": "4691.78", "volume": "13243.35500195", "low": "4541.00", "ask": "4805.03", "open": "4761.67"}

eth_usd = {}

response = urllib.urlopen(url_eth)
data = json.loads(response.read())

eth_usd['market_name'] = 'Bitstamp'
eth_usd['currencies'] = 'ETH-USD'
eth_usd['last_price'] = float(data['last'])
eth_usd['min_ask'] = float(data['ask'])
eth_usd['max_bid'] = float(data['bid'])
eth_usd['last_update'] = str(datetime.datetime.now()).split('.')[0]



with open(currencies_path + 'bitstamp_eth_usd.json', 'w') as outfile:
    json.dump(eth_usd, outfile)

print eth_usd
