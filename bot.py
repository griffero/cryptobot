import telepot
import time
import os
import json
from moneyed import Money, CLP
from moneyed.localization import format_money
from decimal import Decimal
from babel.numbers import format_currency

from locale import *
import locale
setlocale(LC_NUMERIC, 'es_CL.UTF-8')
setlocale(LC_ALL, 'es_CL.UTF-8')
setlocale(LC_MONETARY, 'es_CL.UTF-8')


bot = telepot.Bot('331003353:AAEy6xrXZ-uIRJmq4q-jNVtoe0RjzXlzBSU')
group = '-268121898'

currencies_path = '/root/cryptobot/currencies/'


def display_eth_info(currencies_name):
    usd_clp_rate = ""
    with open(currencies_path + 'usd_clp.json') as data_file:
           data = json.load(data_file)
           usd_clp_rate = float(data['last_rate'])

    with open(currencies_path + currencies_name) as data_file:
           # contenido: {u'max_bid': 3057494, u'last_price': 3104998, u'min_ask': 3104997, u'last_update': u'2017-10-09 23:12:55'}
           data = json.load(data_file)
           market_name = data['market_name']
           currencies = data['currencies']
           out_convert_maxbid = ""
           out_convert_minask = ""
           out_convert_lastprice = ""
           if currencies == "ETH-CLP":
               max_bid_usd = round(data['max_bid']/usd_clp_rate, 2)
               min_ask_usd = round(data['min_ask']/usd_clp_rate, 2)
               last_price_usd = round(data['last_price']/usd_clp_rate, 2)
               out_convert_maxbid = "(USD$%s)" % (str(max_bid_usd))
               out_convert_minask = "(USD$%s)" % (str(min_ask_usd))
               out_convert_lastprice = "(USD$%s)" % (str(last_price_usd))
               max_bid =  format_currency(data['max_bid'], 'CLP', locale='es_CL')
               min_ask =  format_currency(data['min_ask'], 'CLP', locale='es_CL')
               last_price =  format_currency(data['last_price'], 'CLP', locale='es_CL')
           else:
               max_bid =  format_currency(data['max_bid'], 'USD', locale='en_US')
               min_ask =  format_currency(data['min_ask'], 'USD', locale='en_US')
               last_price =  format_currency(data['last_price'], 'USD', locale='en_US')
           last_update = data['last_update']
           #data['min_ask'] = Money(data['max_bid'], 'CLP')
           #data['last_price'] = Money(data['max_bid'], 'CLP')
           return '\n' + "%s %s:\n  - max bid: %s %s\n  - min ask: %s %s\n  - last price: %s %s\n  - Last Update: %s" % (market_name, currencies, max_bid, out_convert_maxbid, min_ask, out_convert_minask, last_price, out_convert_lastprice, last_update)


def display_eth_info_short(currencies_name):
    usd_clp_rate = ""
    with open(currencies_path + 'usd_clp.json') as data_file:
           data = json.load(data_file)
           usd_clp_rate = float(data['last_rate'])

    with open(currencies_path + currencies_name) as data_file:
           # contenido: {u'max_bid': 3057494, u'last_price': 3104998, u'min_ask': 3104997, u'last_update': u'2017-10-09 23:12:55'}
           data = json.load(data_file)
           market_name = data['market_name']
           currencies = data['currencies']
           out_convert_maxbid = ""
           out_convert_minask = ""
           out_convert_lastprice = ""
           if currencies == "ETH-CLP":
               max_bid_usd = round(data['max_bid']/usd_clp_rate, 2)
               min_ask_usd = round(data['min_ask']/usd_clp_rate, 2)
               last_price_usd = round(data['last_price']/usd_clp_rate, 2)
               out_convert_maxbid = "(USD$%s)" % (str(max_bid_usd))
               out_convert_minask = "(USD$%s)" % (str(min_ask_usd))
               out_convert_lastprice = "(USD$%s)" % (str(last_price_usd))
               max_bid =  format_currency(data['max_bid'], 'CLP', locale='es_CL')
               min_ask =  format_currency(data['min_ask'], 'CLP', locale='es_CL')
               last_price =  format_currency(data['last_price'], 'CLP', locale='es_CL')
           else:
               max_bid =  format_currency(data['max_bid'], 'USD', locale='en_US')
               min_ask =  format_currency(data['min_ask'], 'USD', locale='en_US')
               last_price =  format_currency(data['last_price'], 'USD', locale='en_US')
           last_update = data['last_update']
           #data['min_ask'] = Money(data['max_bid'], 'CLP')
           #data['last_price'] = Money(data['max_bid'], 'CLP')
           return '\n' + "*%s*: %s %s (Last Update: %s)" % (market_name, last_price, out_convert_lastprice, last_update)

def send_ethclp_stats():
    out = ""
    out += display_eth_info('eth_clp.json')
    out += display_eth_info('eth_clp_cryptomkt.json')
    out += display_eth_info('bitstamp_eth_usd.json')
    out += display_eth_info('bitfinex_eth_usd.json')
    out += display_eth_info('gdax_eth_usd.json')
    bot.sendMessage(group, out, parse_mode="markdown")

def send_ethclp_stats_short():
    out = ""
    out += display_eth_info_short('eth_clp.json')
    out += display_eth_info_short('eth_clp_cryptomkt.json')
    out += display_eth_info_short('bitstamp_eth_usd.json')
    out += display_eth_info_short('bitfinex_eth_usd.json')
    out += display_eth_info_short('gdax_eth_usd.json')
    bot.sendMessage(group, out, parse_mode="markdown")

def send_btcclp_stats():
             out = ""
             with open(currencies_path + 'btc_clp.json') as data_file:
                    # contenido: {u'max_bid': 3057494, u'last_price': 3104998, u'min_ask': 3104997, u'last_update': u'2017-10-09 23:12:55'}
                    data = json.load(data_file)
                    max_bid =  format_currency(data['max_bid'], 'CLP', locale='es_CL')
                    min_ask =  format_currency(data['min_ask'], 'CLP', locale='es_CL')
                    last_price =  format_currency(data['last_price'], 'CLP', locale='es_CL')
                    last_update = data['last_update']
                    #data['min_ask'] = Money(data['max_bid'], 'CLP')
                    #data['last_price'] = Money(data['max_bid'], 'CLP')
                    out += '\n' + "SURBTC (BTC-CLP):\n  - max bid: %s\n  - min ask: %s\n  - last price: %s\n  - Last Update: %s" % (max_bid, min_ask, last_price, last_update)

             with open(currencies_path + 'bitstamp_btc_usd.json') as data_file:
                    data = json.load(data_file)
                    max_bid =  format_currency(data['max_bid'], 'USD', locale='en_US')
                    min_ask =  format_currency(data['min_ask'], 'USD', locale='en_US')
                    last_price =  format_currency(data['last_price'], 'USD', locale='en_US')
                    last_update = data['last_update']

                    out += '\n' + "Bitstamp (BTC-USD):\n  - max bid: %s\n  - min ask: %s\n  - last price: %s\n  - Last Update: %s" % (max_bid, min_ask, last_price, last_update)

             with open(currencies_path + 'bitfinex_btc_usd.json') as data_file:
                    data = json.load(data_file)
                    max_bid =  format_currency(data['max_bid'], 'USD', locale='en_US')
                    min_ask =  format_currency(data['min_ask'], 'USD', locale='en_US')
                    last_price =  format_currency(data['last_price'], 'USD', locale='en_US')
                    last_update = data['last_update']

                    out += '\n' + "Bitfinex (BTC-USD):\n  - max bid: %s\n  - min ask: %s\n  - last price: %s\n  - Last Update: %s" % (max_bid, min_ask, last_price, last_update)

             with open(currencies_path + 'gdax_btc_usd.json') as data_file:
                    data = json.load(data_file)
                    max_bid =  format_currency(data['max_bid'], 'USD', locale='en_US')
                    min_ask =  format_currency(data['min_ask'], 'USD', locale='en_US')
                    last_price =  format_currency(data['last_price'], 'USD', locale='en_US')
                    last_update = data['last_update']

                    out += '\n' + "GDAX (BTC-USD):\n  - max bid: %s\n  - min ask: %s\n  - last price: %s\n  - Last Update: %s" % (max_bid, min_ask, last_price, last_update)
             bot.sendMessage(group, out)


def send_btcclp_stats_short():
             out = ""
             with open(currencies_path + 'btc_clp.json') as data_file:
                    # contenido: {u'max_bid': 3057494, u'last_price': 3104998, u'min_ask': 3104997, u'last_update': u'2017-10-09 23:12:55'}
                    data = json.load(data_file)
                    max_bid =  format_currency(data['max_bid'], 'CLP', locale='es_CL')
                    min_ask =  format_currency(data['min_ask'], 'CLP', locale='es_CL')
                    last_price =  format_currency(data['last_price'], 'CLP', locale='es_CL')
                    last_update = data['last_update']
                    #data['min_ask'] = Money(data['max_bid'], 'CLP')
                    #data['last_price'] = Money(data['max_bid'], 'CLP')
                    out += '\n' + "SURBTC (BTC-CLP): %s (Last Update: %s)" % (last_price, last_update)

             with open(currencies_path + 'bitstamp_btc_usd.json') as data_file:
                    data = json.load(data_file)
                    max_bid =  format_currency(data['max_bid'], 'USD', locale='en_US')
                    min_ask =  format_currency(data['min_ask'], 'USD', locale='en_US')
                    last_price =  format_currency(data['last_price'], 'USD', locale='en_US')
                    last_update = data['last_update']

                    out += '\n' + "Bitstamp (BTC-USD): %s (Last Update: %s)" % (last_price, last_update)

             with open(currencies_path + 'bitfinex_btc_usd.json') as data_file:
                    data = json.load(data_file)
                    max_bid =  format_currency(data['max_bid'], 'USD', locale='en_US')
                    min_ask =  format_currency(data['min_ask'], 'USD', locale='en_US')
                    last_price =  format_currency(data['last_price'], 'USD', locale='en_US')
                    last_update = data['last_update']

                    out += '\n' + "Bitfinex (BTC-USD): %s (Last Update: %s)" % (last_price, last_update)

             with open(currencies_path + 'gdax_btc_usd.json') as data_file:
                    data = json.load(data_file)
                    max_bid =  format_currency(data['max_bid'], 'USD', locale='en_US')
                    min_ask =  format_currency(data['min_ask'], 'USD', locale='en_US')
                    last_price =  format_currency(data['last_price'], 'USD', locale='en_US')
                    last_update = data['last_update']

                    out += '\n' + "GDAX (BTC-USD): %s (Last Update: %s)" % (last_price, last_update)
             bot.sendMessage(group, out)

def forcerefresh():
             os.system("python /root/cryptobot/update_scripts/surbtc.py")
             bot.sendMessage(group, "Valores SURBTC Actualizados")
             os.system("python /root/cryptobot/update_scripts/cryptomkt.py")
             bot.sendMessage(group, "Valores Crytomkt Actualizados")
             os.system("python /root/cryptobot/update_scripts/bitstamp.py")
             bot.sendMessage(group, "Valores Bitstamp Actualizados")
             os.system("python /root/cryptobot/update_scripts/bitfinex.py")
             bot.sendMessage(group, "Valores Bitfinex Actualizados")
             os.system("python /root/cryptobot/update_scripts/gdax.py")
             bot.sendMessage(group, "Valores GDAX Actualizados")

             send_ethclp_stats()
             send_btcclp_stats()

def getmarkets():
   currencyfiles = []
   markets = {}
   for path, directories, files in os.walk(currencies_path):
     print files
     for file in files:
        if ".json" in file:
          currencyfiles.append(file)
   print currencyfiles
   for currencyfile in currencyfiles:
       with open('/root/cryptobot/currencies/' + currencyfile) as data_file:
          data = json.load(data_file)
          if "currencies" in data:
             currency = {}
             currency[data['currencies']] = {}
             currency[data['currencies']]['last_price'] = data['last_price'] 
             currency[data['currencies']]['max_bid'] = data['max_bid'] 
             currency[data['currencies']]['min_ask'] = data['min_ask'] 
             if data['market_name'] not in markets:
                markets[data['market_name']] = []
                markets[data['market_name']].append(currency)
             else:
                markets[data['market_name']].append(currency) 

   print markets

def removealert(file):
  print '/root/cryptobot/alerts/' + file + ".json"
  if os.path.isfile('/root/cryptobot/alerts/' + file + ".json"):
     os.system("rm /root/cryptobot/alerts/" + file + ".json")
     bot.sendMessage(group, "Alerta %s borrada" % (file))
  else:
     bot.sendMessage(group, "La alerta %s no existe" % (file))


"""
{
  "currency": "BTC-USD",
  "limit": "5650.0",
  "if": "lower"
}
"""
def addalert(exchange, condition, limit):
  selected = 0
  while True:
   if os.path.isfile('/root/cryptobot/alerts/' + str(selected) + '.json'):
     selected += 1
     continue
   break
  filename = str(selected)+'.json'
  opts = {}
  opts["currency"] = exchange
  opts["limit"] = float(limit)
  opts["if"] = condition
  with open('/root/cryptobot/alerts/' + filename, 'w') as outfile:
    json.dump(opts, outfile, indent=3)
  

def getalerts():
   alertfiles = []
   alerts = {}
   for path, directories, files in os.walk('/root/cryptobot/alerts/'):
     for file in files:
        if ".json" in file:
          alertfiles.append(file)
   for alertfile in alertfiles:
       with open('/root/cryptobot/alerts/' + alertfile) as data_file:
          data = json.load(data_file)
          alerts[alertfile] = {}
          alerts[alertfile]['currency'] = data['currency']
          alerts[alertfile]['limit']    = data['limit']
          alerts[alertfile]['if']       = data['if']
   return alerts

def showalerts():
   msg_out = ''
   alertfiles = []
   alerts = getalerts()
   
   msg_out += "Alertas configuradas\n\n"
   for alert in alerts:
     msg_out += "*" + alert + "*:\n"
     msg_out += "  *Currency:* " + alerts[alert]['currency'] + "\n"
     msg_out += "  *Limit:* " + str(float(alerts[alert]['limit'])) + "\n"
     msg_out += "  *If:* " + alerts[alert]['if'] + "\n"
   bot.sendMessage(group, msg_out, parse_mode="markdown")

def arbitraje(btc=1, eth=1):
             out = "Oportunidades de Arbitraje: "
             usd_clp_rate = ""
             with open(currencies_path + 'usd_clp.json') as data_file:
                   data = json.load(data_file)
                   usd_clp_rate = float(data['last_rate'])
             print usd_clp_rate
             ### BITCOIN
             surbtc_btc_max_bid = ""
             surbtc_btc_min_ask = ""
             surbtc_btc_last_price = ""
             bitstamp_btc_max_bid = ""
             bitstamp_btc_min_ask = ""
             bitstamp_btc_last_price = ""

             with open(currencies_path + 'btc_clp.json') as data_file:
                    # contenido: {u'max_bid': 3057494, u'last_price': 3104998, u'min_ask': 3104997, u'last_update': u'2017-10-09 23:12:55'}
                    data = json.load(data_file)
                    surbtc_btc_max_bid =  float(data['max_bid'])
                    surbtc_btc_min_ask =  float(data['min_ask'])
                    surbtc_btc_last_price = float(data['last_price'])
                    #data['min_ask'] = Money(data['max_bid'], 'CLP')
                    #data['last_price'] = Money(data['max_bid'], 'CLP')

             with open(currencies_path + 'bitstamp_btc_usd.json') as data_file:
                    data = json.load(data_file)
                    bitstamp_btc_max_bid =  float(data['max_bid'])
                    bitstamp_btc_min_ask =  float(data['min_ask'])
                    bitstamp_btc_last_price =  float(data['last_price'])
             # Detectar diferencia de ultim precio
             if bitstamp_btc_last_price*usd_clp_rate > surbtc_btc_min_ask:
                    maxbtc = format_currency(int(bitstamp_btc_last_price*btc*usd_clp_rate), 'CLP', locale='es_CL')
                    minbtc = format_currency(int(surbtc_btc_last_price*btc), 'CLP', locale='es_CL')
                    margin = format_currency(int(bitstamp_btc_last_price*btc*usd_clp_rate)-int(surbtc_btc_last_price*btc), 'CLP', locale='es_CL')
                    out +=  "\n" + "  - Al comprar %s BTC en SurBTC a %s, podria venderse en BitStamp a %s y ganar %s" % (btc, minbtc, maxbtc, margin)
             if bitstamp_btc_last_price*usd_clp_rate < surbtc_btc_last_price:
                    maxbtc = format_currency(int(surbtc_btc_last_price*btc), 'CLP', locale='es_CL')
                    minbtc = format_currency(int(bitstamp_btc_last_price*btc*usd_clp_rate), 'CLP', locale='es_CL')
                    margin = format_currency(int(surbtc_btc_last_price*btc-bitstamp_btc_last_price*btc*usd_clp_rate), 'CLP', locale='es_CL')
                    out += "\n" + "  - Al comprar %s BTC en Bitstamp a %s, podria venderse en SurBTC a %s y ganar %s" % (btc, minbtc, maxbtc, margin)


             ### ETH
             surbtc_eth_max_bid = ""
             surbtc_eth_min_ask = ""
             surbtc_eth_last_price = ""
             cryptomkt_eth_max_bid = ""
             cryptomkt_eth_min_ask = ""
             cryptomkt_eth_last_price = ""
             bitstamp_eth_max_bid = ""
             bitstamp_eth_min_ask = ""
             bitstamp_eth_last_price = ""

             with open(currencies_path + 'eth_clp.json') as data_file:
                    # contenido: {u'max_bid': 3057494, u'last_price': 3104998, u'min_ask': 3104997, u'last_update': u'2017-10-09 23:12:55'}
                    data = json.load(data_file)
                    surbtc_eth_max_bid =  float(data['max_bid'])
                    surbtc_eth_min_ask =  float(data['min_ask'])
                    surbtc_eth_last_price = float(data['last_price'])
                    #data['min_ask'] = Money(data['max_bid'], 'CLP')
                    #data['last_price'] = Money(data['max_bid'], 'CLP')

             with open(currencies_path + 'eth_clp_cryptomkt.json') as data_file:
                   # contenido: {u'max_bid': 3057494, u'last_price': 3104998, u'min_ask': 3104997, u'last_update': u'2017-10-09 23:12:55'}
                   data = json.load(data_file)
                   cryptomkt_eth_max_bid =  float(data['max_bid'])
                   cryptomkt_eth_min_ask =  float(data['min_ask'])
                   cryptomkt_eth_last_price = float(data['last_price'])
                   #data['min_ask'] = Money(data['max_bid'], 'CLP')
                   #data['last_price'] = Money(data['max_bid'], 'CLP')

             with open(currencies_path + 'bitstamp_eth_usd.json') as data_file:
                    data = json.load(data_file)
                    bitstamp_eth_max_bid =  float(data['max_bid'])
                    bitstamp_eth_min_ask =  float(data['min_ask'])
                    bitstamp_eth_last_price =  float(data['last_price'])
             # Detectar diferencia de ultim precio
             if bitstamp_eth_last_price*usd_clp_rate > surbtc_eth_last_price:
#                    print "Existe una oportunidad de comprar eth barato en SurBTC y venderlo mas caro en Bitstamp"
                    maxeth = format_currency(int(bitstamp_eth_last_price*eth*usd_clp_rate), 'CLP', locale='es_CL')
                    mineth = format_currency(int(surbtc_eth_last_price*eth), 'CLP', locale='es_CL')
                    margin = format_currency(int(bitstamp_eth_last_price*eth*usd_clp_rate)-int(surbtc_eth_last_price*eth), 'CLP', locale='es_CL')
                    out += '\n' + "  - Al comprar %s ETH en SurBTC a %s, podria venderse en BitStamp a %s y ganar %s" % (eth, mineth, maxeth, margin)
             if bitstamp_eth_last_price*usd_clp_rate < surbtc_eth_last_price:
#                    print "Existe una oportunidad de comprar eth barato en Bitstamp y venderlo mas caro en SurBTC"
                    maxeth = format_currency(int(surbtc_eth_last_price*eth), 'CLP', locale='es_CL')
                    mineth = format_currency(int(bitstamp_eth_last_price*eth*usd_clp_rate), 'CLP', locale='es_CL')
                    margin = format_currency(int(surbtc_eth_last_price*eth-bitstamp_eth_last_price*eth*usd_clp_rate), 'CLP', locale='es_CL')
                    out += '\n' + "  - Al comprar %s ETH en Bitstamp a %s, podria venderse en SurBTC a %s y ganar %s" % (eth, mineth, maxeth, margin)
             if bitstamp_eth_last_price*usd_clp_rate > cryptomkt_eth_last_price:
            #                    print "Existe una oportunidad de comprar eth barato en SurBTC y venderlo mas caro en Bitstamp"
                   maxeth = format_currency(int(bitstamp_eth_last_price*eth*usd_clp_rate), 'CLP', locale='es_CL')
                   mineth = format_currency(int(cryptomkt_eth_last_price*eth), 'CLP', locale='es_CL')
                   margin = format_currency(int(bitstamp_eth_last_price*eth*usd_clp_rate)-int(surbtc_eth_last_price*eth), 'CLP', locale='es_CL')
                   out += '\n' + "  - Al comprar %s ETH en Crytomkt a %s, podria venderse en BitStamp a %s y ganar %s" % (eth, mineth, maxeth, margin)
             if bitstamp_eth_last_price*usd_clp_rate < cryptomkt_eth_last_price:
            #                    print "Existe una oportunidad de comprar eth barato en Bitstamp y venderlo mas caro en Cryptomkt"
                   maxeth = format_currency(int(cryptomkt_eth_last_price*eth), 'CLP', locale='es_CL')
                   mineth = format_currency(int(bitstamp_eth_last_price*eth*usd_clp_rate), 'CLP', locale='es_CL')
                   margin = format_currency(int(cryptomkt_eth_last_price*eth-bitstamp_eth_last_price*eth*usd_clp_rate), 'CLP', locale='es_CL')
                   out += '\n' + "  - Al comprar %s ETH en Bitstamp a %s, podria venderse en Crytomkt a %s y ganar %s" % (eth, mineth, maxeth, margin)


             # Arbitraje BCI
             monto_original = 1000000
             monto_usd = monto_original/usd_clp_rate
             costo_transferencia = 55
             #
             comision_bitstamp = (monto_usd - costo_transferencia)*0.0005
             if comision_bitstamp < 7.5:
               comision_bitstamp = 7.5
             monto_efectivo = monto_usd - costo_transferencia - comision_bitstamp
             cantidad_eth_a_comprar = round((monto_efectivo*0.9965/bitstamp_eth_last_price), 6)
             liquidacion_surbtc = (cantidad_eth_a_comprar)*0.9945*surbtc_eth_max_bid
             out += "\n\nCon un presupuesto de $1.000.000, se puede transferir por BCI a bitstamp, logrando comprar ETH%s para luego liquidar en surBTC a %s" % (str(cantidad_eth_a_comprar), format_currency(liquidacion_surbtc, 'CLP', locale='es_CL')) 
             out += "\n- Costo BCI: %s" % (str(costo_transferencia))
             out += "\n- Costo Deposito Bitstamp: USD$%s" % (str(comision_bitstamp))
             out += "\n- Costo Orden de Compra Bitstamp: USD$%s" % (str(monto_efectivo*0.0035))
             out += "\n- Costo Orden de Venta SurBTC: ETH%s" % (str(cantidad_eth_a_comprar*0.0055))
             out += '\n\n' + "Tasa de cambio: 1 USD = %s CLP (Yahoo Finance)" % (usd_clp_rate)
             out += '\n' + 'WIP: Incluir costos de transacciones en calculo'
             #print out
             bot.sendMessage(group, out)


def handle(msg):
   content_type, chat_type, chat_id = telepot.glance(msg)
   print content_type
   print chat_type
   print chat_id
   if content_type.strip() == 'text' and chat_type.strip() == 'group' and str(chat_id) == '-268121898':
         if "/eth" == msg["text"]:
             send_ethclp_stats_short()
             return
         if "/btc" == msg["text"]:
             send_btcclp_stats_short()
             return
         if "/eth long" == msg["text"]:
             send_ethclp_stats()
             return
         if "/btc long" == msg["text"]:
             send_btcclp_stats()
             return
         if "/forcerefresh" == msg["text"]:
             forcerefresh()
             return
         if "/alerts" == msg["text"]:
             mensaje = "Uso: \n- /alerts show\n- /alerts remove"
             bot.sendMessage(group, mensaje)
         if "/alerts show" == msg["text"]:
             showalerts()
             return
         if "/alerts remove" in msg["text"]:
             if len(msg["text"].split(" ")) == 3:
                cmd, cmd2, file = msg["text"].split(" ")
                removealert(file)
             else:
                bot.sendMessage(group, "Uso: /alerts remove <Nombre alerta sin .json>")
             return
         if "/alerts add" in msg["text"]:
             if len(msg["text"].split(" ")) == 5:
                arg0, arg1, exchange, condition, limit = msg["text"].split(" ")
                condition = condition.lower()
                if condition not in ["upper", "lower"]:
                   bot.sendMessage(group, "Uso: /alerts add <BTC-USD> <upper|lower> <limit>")
                   return
                try:
                   limit = float(limit)
                except:
                   bot.sendMessage(group, "Uso: /alerts add <BTC-USD> <upper|lower> <limit>")
                   return
                addalert(exchange, condition, limit) 
             else:
                bot.sendMessage(group, "Uso: /alerts add <BTC-USD> <upper|lower> <limit>")
             return
         if "/arbitraje" in msg["text"]:
             if "/arbitraje" == msg["text"]:
                arbitraje()
             if len(msg["text"].split(" ")) == 3:
                cmd, btc, eth = msg["text"].split(" ")
                arbitraje(float(btc), float(eth))
             return
         print msg["text"]
         print msg["date"]


bot.message_loop(handle)

while 1:
   time.sleep(10)
