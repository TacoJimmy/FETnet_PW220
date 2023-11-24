# coding:utf-8
import codecs
import json
import ssl
import paho.mqtt.client as mqtt
import time
import FET_modbustcp


def PowerLoop():
    with open('static/data/PowerMeter.json', 'r') as f:
        data = json.load(f)
    f.close
    return data

def ReadMqttInfor():
    with open('static/data/mqttinfor.json', 'r') as f:
        data = json.load(f)
    f.close
    return data
def ReadMqttInfor():
    with open('static/data/mqttinfor2.json', 'r') as f:
        data = json.load(f)
    f.close
    return data

def MqttSend(mod_payload,loop):
    Mqttinfor = ReadMqttInfor()
    try:
        client = mqtt.Client('', True, None, mqtt.MQTTv31)
        client.username_pw_set(Mqttinfor['appInfo']['MQTT_UserName'], Mqttinfor['appInfo']['MQTT_Password'])
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        client.tls_set_context(context)
        client.connect(Mqttinfor['appInfo']['MQTT_url'], Mqttinfor['appInfo']['MQTT_Port'], 60)
        client.loop_start()
        time.sleep(1)
        client.on_connect
        
        for i in range(loop):
            data03 = client.publish(Mqttinfor['appInfo']['MQTT_topic'],json.dumps(mod_payload[i]))
        time.sleep(1)
        
        client.loop_stop()
        client.disconnect()
        time.sleep(1)

        
    except:
        print ('error')
        return ('error')
    

def MqttSend2(mod_payload,loop):
    Mqttinfor = ReadMqttInfor()
    try:
        client2 = mqtt.Client('', True, None, mqtt.MQTTv31)
        client2.username_pw_set(Mqttinfor['appInfo']['MQTT_UserName'], Mqttinfor['appInfo']['MQTT_Password'])
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        client2.tls_set_context(context)
        client2.connect(Mqttinfor['appInfo']['MQTT_url'], Mqttinfor['appInfo']['MQTT_Port'], 60)
        client2.loop_start()
        time.sleep(1)
        client2.on_connect
        
        for i in range(loop):
            data03 = client2.publish(Mqttinfor['appInfo']['MQTT_topic'],json.dumps(mod_payload[i]))
        time.sleep(1)
        
        client2.loop_stop()
        client2.disconnect()
        time.sleep(1)

        
    except:
        print ('error')
        return ('error')
'''
def MqttMainSend(mod_payload):
    Mqttinfor = ReadMqttInfor()
    try:
        client = mqtt.Client('', True, None, mqtt.MQTTv31)
        client.username_pw_set(Mqttinfor['appInfo']['MQTT_UserName'], Mqttinfor['appInfo']['MQTT_Password'])
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        client.tls_set_context(context)
        client.connect(Mqttinfor['appInfo']['MQTT_url'], Mqttinfor['appInfo']['MQTT_Port'], 60)
        client.loop_start()
        time.sleep(1)
        data02 = client.on_connect
        data03 = client.publish(Mqttinfor['appInfo']['MQTT_topic'],json.dumps(mod_payload[0]))
        time.sleep(2)
        data03 = client.publish(Mqttinfor['appInfo']['MQTT_topic'],json.dumps(mod_payload[1]))
        time.sleep(2)
        client.loop_stop()
        client.disconnect()
        time.sleep(1)
    except:
        print ('error')
        return ('error')

def MqttACSend(mod_payload):
    Mqttinfor = ReadMqttInfor()
    try:
        client = mqtt.Client('', True, None, mqtt.MQTTv31)
        client.username_pw_set(Mqttinfor['appInfo']['MQTT_UserName'], Mqttinfor['appInfo']['MQTT_Password'])
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        client.tls_set_context(context)
        client.connect(Mqttinfor['appInfo']['MQTT_url'], Mqttinfor['appInfo']['MQTT_Port'], 60)
        client.loop_start()
        time.sleep(1)
        data02 = client.on_connect
        data03 = client.publish(Mqttinfor['appInfo']['MQTT_topic'],json.dumps(mod_payload[0]))
        time.sleep(2)
        data03 = client.publish(Mqttinfor['appInfo']['MQTT_topic'],json.dumps(mod_payload[1]))
        time.sleep(2)
        client.loop_stop()
        client.disconnect()
        time.sleep(1)
    except:
        print ('error')
        return ('error')


'''
def MqttPublish():
    SubLoop01 = FET_modbustcp.getPowerLoop01('192.5.1.120',502)
    print(SubLoop01)
    print("01_ok")
    MqttSend(SubLoop01,14)
    #MqttSend2(SubLoop01,14)
    print("02_ok")
    MainLoop01 = FET_modbustcp.getPowerMainLoop01('192.5.1.120', 502)
    print("03_ok")
    MqttSend(MainLoop01,1)
    #MqttSend2(MainLoop01,1)
    print("04_ok")
    MainLoop = IPC_Loop01()
    print("05_ok")
    MqttSend(MainLoop,1)
    #MqttSend2(MainLoop,1)
    print("06_ok")

def IPC_Loop01():
    PowerPayload ={}
    clamp=[{"voltage":{}},{"voltage":{}},{"voltage":{}},
           {"voltage":{}},{"voltage":{}},{"voltage":{}},
           {"voltage":{}},{"voltage":{}},{"voltage":{}},
           {"voltage":{}},{"voltage":{}},{"voltage":{}},
           {"voltage":{}},{"voltage":{}}]
    try:
        
        
        with open('static/data/PowerSubLoop01.json', 'r') as a:
            subpower01 = json.load(a)
        a.close
        with open('static/data/PowerSubLoop02.json', 'r') as b:
            subpower02 = json.load(b)
        b.close
        with open('static/data/PowerSubLoop03.json', 'r') as a:
            subpower03 = json.load(a)
        a.close
        with open('static/data/PowerSubLoop04.json', 'r') as b:
            subpower04 = json.load(b)
        b.close
        with open('static/data/PowerSubLoop05.json', 'r') as a:
            subpower05 = json.load(a)
        a.close
        with open('static/data/PowerSubLoop06.json', 'r') as b:
            subpower06 = json.load(b)
        b.close
        with open('static/data/PowerSubLoop07.json', 'r') as a:
            subpower07 = json.load(a)
        a.close
        with open('static/data/PowerSubLoop08.json', 'r') as b:
            subpower08 = json.load(b)
        b.close
        with open('static/data/PowerSubLoop09.json', 'r') as a:
            subpower09 = json.load(a)
        a.close
        with open('static/data/PowerSubLoop10.json', 'r') as b:
            subpower10 = json.load(b)
        b.close
        with open('static/data/PowerSubLoop11.json', 'r') as a:
            subpower11 = json.load(a)
        a.close
        with open('static/data/PowerSubLoop12.json', 'r') as b:
            subpower12 = json.load(b)
        b.close
        with open('static/data/PowerSubLoop13.json', 'r') as a:
            subpower13 = json.load(a)
        a.close
        with open('static/data/PowerSubLoop14.json', 'r') as b:
            subpower14 = json.load(b)
        b.close
        
        with open('static/data/PowerMainLoop01.json', 'r') as b:
            mainpower01 = json.load(b)
        b.close
        
        with open('static/data/power_dm.json', 'r') as b:
            powerdm = json.load(b)
        b.close
        
        CT_Power = subpower01["power"]+subpower02["power"]+subpower03["power"]+subpower07["power"]
        CHP_Power = subpower04["power"]+subpower05["power"]+subpower06["power"]+subpower08["power"]+subpower09["power"]
        CWP_Power = subpower10["power"]+subpower11["power"]+subpower12["power"]+subpower13["power"]+subpower14["power"]
        
        CT_energy = subpower01["energy"]+subpower02["energy"]+subpower03["energy"]+subpower07["energy"]
        CHP_energy = subpower04["energy"]+subpower05["energy"]+subpower06["energy"]+subpower08["energy"]+subpower09["energy"]
        CWP_energy = subpower10["energy"]+subpower11["energy"]+subpower12["energy"]+subpower13["energy"]+subpower14["energy"]
        
        clamp[0]["power"] = mainpower01["power"]
        clamp[0]["energy"] = mainpower01["energy"]
        clamp[0]["power_dm"] = powerdm["power_dm"]
        clamp[0]["CT_Power"] = CT_Power
        clamp[0]["CT_energy"] = CT_energy
        clamp[0]["CT_Power_p"] = round(CT_Power / mainpower01["power"],1)
        clamp[0]["CHP_Power"] = CHP_Power
        clamp[0]["CHP_energy"] = CHP_energy
        clamp[0]["CHP_Power_p"] = CHP_Power / mainpower01["power"]
        clamp[0]["CWP_Power"] = CWP_Power
        clamp[0]["CWP_energy"] = CWP_energy
        clamp[0]["CWP_Power_p"] = CWP_Power / mainpower01["power"]
        
    
        PowerPayload[0] = [{"access_token": "GkWtbPJ31C4rca1OVIVm",
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[0]}]}]
        
        with open('static/data/ipc.json', 'w') as f:
            json.dump(PowerPayload[0][0]["data"][0]["values"], f)
        f.close
        print (PowerPayload)
        return PowerPayload
    except:
        pass
    
    
'''


def Pub_infor():
    try:
        Mqttinfor = ReadMqttInfor()
        PowerInfor = PowerLoop()
        MainLoop01  = [
            {"access_token": PowerInfor["MainLoop01"]["access_token"],
             "app": PowerInfor["MainLoop01"]["app"],
             "type": PowerInfor["MainLoop01"]["type"],
             "data": PowerInfor["MainLoop01"]["data"]}]
        print (Mqttinfor['appInfo']['MQTT_UserName'])
    
        client = mqtt.Client('', True, None, mqtt.MQTTv31)
        client.username_pw_set(Mqttinfor['appInfo']['MQTT_UserName'], Mqttinfor['appInfo']['MQTT_Password'])
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        client.tls_set_context(context)
        client.connect(Mqttinfor['appInfo']['MQTT_url'], Mqttinfor['appInfo']['MQTT_Port'], 60)
        client.loop_start()
        time.sleep(1)
        data02 = client.on_connect
        data03 = client.publish(Mqttinfor['appInfo']['MQTT_topic'],json.dumps(MainLoop01))
        time.sleep(3)
        client.loop_stop()
        client.disconnect()
        time.sleep(10)
        return ('OK')
    except:
        return ('error')
'''
   
if __name__ == '__main__':
    while True:
        SubLoop01 = FET_modbustcp.getPowerLoop01('192.5.1.120',502)
        print(SubLoop01)
        print("01_ok")
        '''
        PowerPayload ={}
        clamp=[{"voltage":{}},{"voltage":{}},{"voltage":{}},
           {"voltage":{}},{"voltage":{}},{"voltage":{}},
           {"voltage":{}},{"voltage":{}},{"voltage":{}},
           {"voltage":{}},{"voltage":{}},{"voltage":{}},
           {"voltage":{}},{"voltage":{}}]
        
        with open('static/data/PowerSubLoop14.json', 'r') as a:
            subpower01 = json.load(a)
        a.close
        with open('static/data/PowerMainLoop01.json', 'r') as a:
            mainpower01 = json.load(a)
        a.close
        
        clamp[0]["power"] = mainpower01["power"]
        clamp[0]["power_loop01"] = subpower01["power"]
        clamp[0]["power_loop01_p"] = round(subpower01["power"] / mainpower01["power"]*100,1)
        print (clamp[0])
        time.sleep(10)
        '''