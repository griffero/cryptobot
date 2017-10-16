import time
import os


while True:
             try: 
               os.system("python /root/cryptobot/update_scripts/surbtc.py")
               print "Valores SURBTC Actualizados"
             except:
               pass
             try:
               os.system("python /root/cryptobot/update_scripts/bitstamp.py")
               print "Valores Bitstamp Actualizados"
             except:
               pass
             try:
               os.system("python /root/cryptobot/update_scripts/cryptomkt.py")
               print "Valores Cryptomkt Actualizados"
             except:
               pass
             try:
               os.system("python /root/cryptobot/update_scripts/usdclp.py")
               print "Valores USD-CLP Actualizados"
             except:
               pass
             time.sleep(60)
