import time
import os


while True:
             os.system("python /root/cryptobot/update_scripts/surbtc.py")
             print "Valores SURBTC Actualizados"
             os.system("python /root/cryptobot/update_scripts/bitstamp.py")
             print "Valores Bitstamp Actualizados"
             time.sleep(60)
