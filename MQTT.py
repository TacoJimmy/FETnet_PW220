# coding:utf-8
import codecs
import json
import ssl
import paho.mqtt.client as mqtt
import time

def count_dm():
    
    energy_now = 20
    
    with open('static/data/power_dm.json', 'r') as f:
        power_energy_last = json.load(f)
    f.close
    
    dm_now = energy_now - power_energy_last["power_energy"]
    Payload = {"power_energy":energy_now, "power_dm":dm_now}
    
    with open('static/data/power_dm.json', 'w') as f:
            json.dump(Payload, f)
    f.close

    return Payload

if __name__ == '__main__':
    while True:
      print (count_dm())  
      time.sleep(5)
