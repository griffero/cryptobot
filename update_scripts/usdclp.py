import urllib2, json, datetime

url_clp = "http://download.finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s=USDCLP=X"
# OUTPUT: "USDCLP=X",633.7000,"10/9/2017","5:25pm"



currencies_path = "/root/cryptobot/currencies/"

# Datos BTC-CLP
# Output: {u'ticker': {u'max_bid': [u'3075000.0', u'CLP'], u'last_price': [u'3075000.0', u'CLP'], u'min_ask': [u'3110000.0', u'CLP'], u'volume': [u'19.47938755', u'BTC'], u'price_variation_7d': u'0.075', u'price_variation_24h': u'0.049'}}
response = urllib2.urlopen(url_clp, timeout=3.0)

data = response.read().split(",")
print data

usd_clp = {}

usd_clp['last_rate'] = data[1]


with open(currencies_path + 'usd_clp.json', 'w') as outfile:
    json.dump(usd_clp, outfile)

print usd_clp
