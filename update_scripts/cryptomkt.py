import urllib2, json, datetime

url_eth = "https://api.cryptomkt.com/v1/ticker?market=ETHCLP"

currencies_path = "/root/cryptobot/currencies/"

# Datos BTC-ETH
# Output: {u'ticker': {u'max_bid': [u'190000.0', u'CLP'], u'last_price': [u'190000.0', u'CLP'], u'min_ask': [u'191864.08', u'CLP'], u'volume': [u'109.601386099', u'ETH'], u'price_variation_7d': u'-0.048', u'price_variation_24h': u'-0.032'}}

eth_clp = {}

response = urllib2.urlopen(url_eth, timeout=5.0)
data = json.loads(response.read())


eth_clp['market_name'] = 'Cryptomkt'
eth_clp['currencies'] = 'ETH-CLP'
eth_clp['last_price'] = int(round(float(data['data'][0]['last_price']),0))
eth_clp['min_ask'] = int(round(float(data['data'][0]['ask']),0))
eth_clp['max_bid']  = int(round(float(data['data'][0]['bid']),0))
eth_clp['last_update'] = str(datetime.datetime.now()).split('.')[0]

with open(currencies_path + 'eth_clp_cryptomkt.json', 'w') as outfile:
    json.dump(eth_clp, outfile)

print eth_clp
