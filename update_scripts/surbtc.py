import urllib, json, datetime

url_btc = "https://www.surbtc.com/api/v2/markets/btc-clp/ticker.json"
url_eth = "https://www.surbtc.com/api/v2/markets/eth-clp/ticker.json"

currencies_path = "/root/cryptobot/currencies/"

# Datos BTC-CLP
# Output: {u'ticker': {u'max_bid': [u'3075000.0', u'CLP'], u'last_price': [u'3075000.0', u'CLP'], u'min_ask': [u'3110000.0', u'CLP'], u'volume': [u'19.47938755', u'BTC'], u'price_variation_7d': u'0.075', u'price_variation_24h': u'0.049'}}
response = urllib.urlopen(url_btc)
data = json.loads(response.read())

btc_clp = {}

btc_clp['last_price'] = int(round(float(data['ticker']['last_price'][0]),0))
btc_clp['min_ask'] = int(round(float(data['ticker']['min_ask'][0]),0))
btc_clp['max_bid']  = int(round(float(data['ticker']['max_bid'][0]),0))
btc_clp['last_update'] = str(datetime.datetime.now()).split('.')[0]




with open(currencies_path + 'btc_clp.json', 'w') as outfile:
    json.dump(btc_clp, outfile)

print btc_clp


#print data

# Datos BTC-ETH
# Output: {u'ticker': {u'max_bid': [u'190000.0', u'CLP'], u'last_price': [u'190000.0', u'CLP'], u'min_ask': [u'191864.08', u'CLP'], u'volume': [u'109.601386099', u'ETH'], u'price_variation_7d': u'-0.048', u'price_variation_24h': u'-0.032'}}

eth_clp = {}

response = urllib.urlopen(url_eth)
data = json.loads(response.read())

eth_clp['market_name'] = 'SURBTC'
eth_clp['currencies'] = 'ETH-CLP'
eth_clp['last_price'] = int(round(float(data['ticker']['last_price'][0]),0))
eth_clp['min_ask'] = int(round(float(data['ticker']['min_ask'][0]),0))
eth_clp['max_bid']  = int(round(float(data['ticker']['max_bid'][0]),0))
eth_clp['last_update'] = str(datetime.datetime.now()).split('.')[0]


with open(currencies_path + 'eth_clp.json', 'w') as outfile:
    json.dump(eth_clp, outfile)

print eth_clp
