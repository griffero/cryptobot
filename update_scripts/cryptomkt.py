import urllib, json, datetime

url_eth = "https://api.cryptomkt.com/v1/ticker?market=ETHCLP"

currencies_path = "/root/cryptobot/currencies/"

# Datos BTC-ETH
# Output: {u'ticker': {u'max_bid': [u'190000.0', u'CLP'], u'last_price': [u'190000.0', u'CLP'], u'min_ask': [u'191864.08', u'CLP'], u'volume': [u'109.601386099', u'ETH'], u'price_variation_7d': u'-0.048', u'price_variation_24h': u'-0.032'}}

eth_clp = {}

response = urllib.urlopen(url_eth)
data = json.loads(response.read())

eth_clp['last_price'] = int(round(float(data['ticker']['last_price'][0]),0))
eth_clp['min_ask'] = int(round(float(data['ticker']['ask'][0]),0))
eth_clp['max_bid']  = int(round(float(data['ticker']['bid'][0]),0))
eth_clp['timestamp'] = str(datetime.datetime.now()).split('.')[0]

with open(currencies_path + 'eth_clp_cryptomkt.json', 'w') as outfile:
    json.dump(eth_clp, outfile)

print eth_clp
