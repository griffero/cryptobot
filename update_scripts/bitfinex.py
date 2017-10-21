import urllib2, json, datetime

# https://api.bitfinex.com/v2/tickers?symbols=tBTCUSD
url_btc = "https://api.bitfinex.com/v2/tickers?symbols=tBTCUSD,tETHUSD"
url_eth = "https://www.bitstamp.net/api/v2/ticker/ethusd/"

currencies_path = "/root/cryptobot/currencies/"

headers = { 'User-Agent': 'curl/7.38.0' }

# Datos BTC-CLP
# Output: {"high": "4865.00", "last": "4805.04", "timestamp": "1507604582", "bid": "4800.17", "vwap": "4691.78", "volume": "13243.35500195", "low": "4541.00", "ask": "4805.03", "open": "4761.67"}
req = urllib2.Request(url_btc, None, headers)
response = urllib2.urlopen(req, timeout=4.5)

data = json.loads(response.read())

#
#  [
#    SYMBOL,
#    BID, 
#    BID_SIZE, 
#    ASK, 
#    ASK_SIZE, 
#    DAILY_CHANGE, 
#    DAILY_CHANGE_PERC, 
#    LAST_PRICE, 
#    VOLUME, 
#    HIGH, 
#    LOW
#  ],

data_btc = data[0]
data_eth = data[1]
print data_btc
print data_eth


btc_usd = {}

btc_usd['market_name'] = 'Bitfinex'
btc_usd['currencies'] = 'BTC-USD'
btc_usd['last_price'] = float(data_btc[7])
btc_usd['min_ask'] = float(data_btc[3])
btc_usd['max_bid'] = float(data_btc[1])
btc_usd['last_update'] = str(datetime.datetime.now()).split('.')[0]




with open(currencies_path + 'bitfinex_btc_usd.json', 'w') as outfile:
    json.dump(btc_usd, outfile)

print btc_usd

eth_usd = {}

eth_usd['market_name'] = 'Bitfinex'
eth_usd['currencies'] = 'ETH-USD'
eth_usd['last_price'] = float(data_eth[7])
eth_usd['min_ask'] = float(data_eth[3])
eth_usd['max_bid'] = float(data_eth[1])
eth_usd['last_update'] = str(datetime.datetime.now()).split('.')[0]



with open(currencies_path + 'bitfinex_eth_usd.json', 'w') as outfile:
    json.dump(eth_usd, outfile)

print eth_usd
