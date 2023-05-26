# coding:utf-8
import codecs
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import struct
import paho.mqtt.client as mqtt
import random
import json  
import datetime 
import time

def conver32(LSB,MSB):
    conv32value = LSB + ( MSB << 16 )
    return (conv32value)

def ReadFloat(*args,reverse=False):
    for n,m in args:
        n,m = '%04x'%n,'%04x'%m
    if reverse:
        v = n + m
    else:
        v = m + n
    y_bytes = bytes.fromhex(v)
    y = struct.unpack('!f',y_bytes)[0]
    y = round(y,6)
    return y

def PowerLoop():
    with open('static/data/PowerMeter.json', 'r') as f:
        data = json.load(f)
    f.close
    return data

def getPowerLoop01(HOST_Addr, HOST_Port):
    
    data = [[0]*24 for i in range(14)]
    clamp_data = [0]*14
    PowerPayload = {}
    clamp=[{"voltage":{}},{"voltage":{}},{"voltage":{}},{"voltage":{}},{"voltage":{}},{"voltage":{}},
           {"voltage":{}},{"voltage":{}},{"voltage":{}},{"voltage":{}},{"voltage":{}},{"voltage":{}},
           {"voltage":{}},{"voltage":{}},]
    try:
        master = modbus_tcp.TcpMaster(host=HOST_Addr,port=HOST_Port)
        master.set_timeout(5.0)
        for i in range(14):
            clamp_data[i] = master.execute(1, cst.READ_HOLDING_REGISTERS, i*48, 48)
        for j in range(14):
            for i in range(24):
                data[j][i] = ReadFloat((clamp_data[j][i*2],clamp_data[j][i*2+1]))



        #print (clamp_data)
        '''
        for i in range(27):
            clamp32[i] = ReadFloat((clamp_data[i*2+1], clamp_data[i*2]))
        '''
        for i in range(14):
            clamp[i]["voltage"]=round(data[i][0])
            clamp[i]["current_r"]=round(data[i][7])
            clamp[i]["current_s"]=round(data[i][13])
            clamp[i]["current_t"]=round(data[i][19])
            clamp[i]["temperature_r"]=round(data[i][11])
            clamp[i]["temperature_s"]=round(data[i][17])
            clamp[i]["temperature_t"]=round(data[i][23])
            clamp[i]["battery_r"]=2
            clamp[i]["battery_s"]=2
            clamp[i]["battery_t"]=2
            clamp[i]["power"]= round(data[i][2])
            clamp[i]["pf"]= round(data[i][3],2)
            clamp[i]["alive"]= 1
            clamp[i]["energy"]= round(data[i][4])
            
            
    except:
        for i in range(14):
            clamp[i]["voltage"]=i
            clamp[i]["current_r"]=i
            clamp[i]["current_s"]=i
            clamp[i]["current_t"]=i
            clamp[i]["temperature_r"]=i
            clamp[i]["temperature_s"]=i
            clamp[i]["temperature_t"]=i
            clamp[i]["battery_r"]=i
            clamp[i]["battery_s"]=i
            clamp[i]["battery_t"]=i
            clamp[i]["power"]= i
            clamp[i]["pf"]= i
            clamp[i]["alive"]= 2
            clamp[i]["energy"]= i
            
            print ("error_"+str(i))
    with open('static/data/loopname.json', 'r') as f:
        loop_name = json.load(f)
    f.close
    
    clamp[0]["Loop_name"] = loop_name["loop01"]
    clamp[1]["Loop_name"] = loop_name["loop02"]
    clamp[2]["Loop_name"] = loop_name["loop03"]
    clamp[3]["Loop_name"] = loop_name["loop04"]
    clamp[4]["Loop_name"] = loop_name["loop05"]
    clamp[5]["Loop_name"] = loop_name["loop06"]
    clamp[6]["Loop_name"] = loop_name["loop07"]
    clamp[7]["Loop_name"] = loop_name["loop08"]
    clamp[8]["Loop_name"] = loop_name["loop09"]
    clamp[9]["Loop_name"] = loop_name["loop10"]
    clamp[10]["Loop_name"] = loop_name["loop11"]
    clamp[11]["Loop_name"] = loop_name["loop12"]
    clamp[12]["Loop_name"] = loop_name["loop13"]
    clamp[13]["Loop_name"] = loop_name["loop14"]
    
    with open('static/data/looptoken.json', 'r') as f:
        loop_token = json.load(f)
    f.close
    
    
    PowerPayload[0] = [{"access_token": loop_token["loop01"],
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[0]}]}]
    PowerPayload[1] = [{"access_token": loop_token["loop02"],
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[1]}]}]
    PowerPayload[2] = [{"access_token": loop_token["loop03"],
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[2]}]}]
    PowerPayload[3] = [{"access_token": loop_token["loop04"],
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[3]}]}]
    PowerPayload[4] = [{"access_token": loop_token["loop05"],
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[4]}]}]
    PowerPayload[5] = [{"access_token": loop_token["loop06"],
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[5]}]}]
    PowerPayload[6] = [{"access_token": loop_token["loop07"],
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[6]}]}]
    PowerPayload[7] = [{"access_token": loop_token["loop08"],
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[7]}]}]
    PowerPayload[8] = [{"access_token": loop_token["loop09"],
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[8]}]}]
    PowerPayload[9] = [{"access_token": loop_token["loop10"],
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[9]}]}]
    PowerPayload[10] = [{"access_token": loop_token["loop11"],
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[10]}]}]
    PowerPayload[11] = [{"access_token": loop_token["loop12"],
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[11]}]}]
    PowerPayload[12] = [{"access_token": loop_token["loop13"],
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[12]}]}]
    PowerPayload[13] = [{"access_token": loop_token["loop14"],
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[13]}]}]
    
    with open('static/data/PowerSubLoop01.json', 'w') as f:
        json.dump(PowerPayload[0][0]["data"][0]["values"], f)
    f.close
    with open('static/data/PowerSubLoop02.json', 'w') as f:
        json.dump(PowerPayload[1][0]["data"][0]["values"], f)
    f.close
    with open('static/data/PowerSubLoop03.json', 'w') as f:
        json.dump(PowerPayload[2][0]["data"][0]["values"], f)
    f.close
    with open('static/data/PowerSubLoop04.json', 'w') as f:
        json.dump(PowerPayload[3][0]["data"][0]["values"], f)
    f.close
    with open('static/data/PowerSubLoop05.json', 'w') as f:
        json.dump(PowerPayload[4][0]["data"][0]["values"], f)
    f.close
    with open('static/data/PowerSubLoop06.json', 'w') as f:
        json.dump(PowerPayload[5][0]["data"][0]["values"], f)
    f.close
    with open('static/data/PowerSubLoop07.json', 'w') as f:
        json.dump(PowerPayload[6][0]["data"][0]["values"], f)
    f.close
    with open('static/data/PowerSubLoop08.json', 'w') as f:
        json.dump(PowerPayload[7][0]["data"][0]["values"], f)
    f.close
    with open('static/data/PowerSubLoop09.json', 'w') as f:
        json.dump(PowerPayload[8][0]["data"][0]["values"], f)
    f.close
    with open('static/data/PowerSubLoop10.json', 'w') as f:
        json.dump(PowerPayload[9][0]["data"][0]["values"], f)
    f.close
    with open('static/data/PowerSubLoop11.json', 'w') as f:
        json.dump(PowerPayload[10][0]["data"][0]["values"], f)
    f.close
    with open('static/data/PowerSubLoop12.json', 'w') as f:
        json.dump(PowerPayload[11][0]["data"][0]["values"], f)
    f.close
    with open('static/data/PowerSubLoop13.json', 'w') as f:
        json.dump(PowerPayload[12][0]["data"][0]["values"], f)
    f.close
    with open('static/data/PowerSubLoop14.json', 'w') as f:
        json.dump(PowerPayload[13][0]["data"][0]["values"], f)
    f.close
    
    print (PowerPayload[3][0]["data"][0]["values"]["current_s"])
    
    return PowerPayload


def GetPowerEnergy(HOST_Addr, HOST_Port):
    
    master = modbus_tcp.TcpMaster(host=HOST_Addr,port=HOST_Port)
    master.set_timeout(5.0)
    clamp_data = master.execute(1, cst.READ_HOLDING_REGISTERS, 680, 2)
    
    
    power_engergy = ReadFloat((clamp_data[0],clamp_data[1]))
            
    return power_engergy

def getPowerMainLoop01(HOST_Addr, HOST_Port):
    
    data = [[0]*24 for i in range(2)]
    clamp_data = [0]*2
    PowerPayload = {}
    clamp=[{"voltage":{}},{"voltage":{}}]
    try:
        master = modbus_tcp.TcpMaster(host=HOST_Addr,port=HOST_Port)
        master.set_timeout(5.0)
        
        
        
        for i in range(1):
            clamp_data[i] = master.execute(1, cst.READ_HOLDING_REGISTERS, 672, 48)
        
        for j in range(1):
            for i in range(24):
                data[j][i] = ReadFloat((clamp_data[0][i*2],clamp_data[0][i*2+1]))

        for i in range(1):
            clamp[i]["voltage"]=round(data[i][0])
            clamp[i]["current_r"]=round(data[i][7])
            clamp[i]["current_s"]=round(data[i][13])
            clamp[i]["current_t"]=round(data[i][19])
            clamp[i]["temperature_r"]="NA"
            clamp[i]["temperature_s"]="NA"
            clamp[i]["temperature_t"]="NA"
            clamp[i]["battery_r"]=2
            clamp[i]["battery_s"]=2
            clamp[i]["battery_t"]=2
            clamp[i]["power"]= round(data[i][2])
            clamp[i]["pf"]= round(data[i][3],2)
            clamp[i]["alive"]= 1
            clamp[i]["energy"]= round(data[i][4])
            
            
    except:
        
        for i in range(1):
            clamp[i]["voltage"]=0
            clamp[i]["current_r"]=0
            clamp[i]["current_s"]=0
            clamp[i]["current_t"]=0
            clamp[i]["temperature_r"]=0
            clamp[i]["temperature_s"]=0
            clamp[i]["temperature_t"]=0
            clamp[i]["battery_r"]=0
            clamp[i]["battery_s"]=0
            clamp[i]["battery_t"]=0
            clamp[i]["power"]= 0
            clamp[i]["pf"]= 0
            clamp[i]["alive"]= 2
            clamp[i]["energy"]= 0
    with open('static/data/mainloopname.json', 'r') as f:
        loop_name = json.load(f)
    f.close
    
    clamp[0]["Loop_name"] = loop_name["loop01"]
    
    with open('static/data/mainlooptoken.json', 'r') as f:
        loop_token = json.load(f)
    f.close
    
    
    PowerPayload[0] = [{"access_token": loop_token["loop01"],
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[0]}]}]

    
    with open('static/data/PowerMainLoop01.json', 'w') as f:
        json.dump(PowerPayload[0][0]["data"][0]["values"], f)
    f.close
    
    return PowerPayload

def getmodbustcp(HOST_Addr, HOST_Port):
    data = [[0]*24 for i in range(14)]
    clamp_data = [0]*14
    PowerPayload = {}
    clamp=[{"voltage":{}},{"voltage":{}}]
    
    master = modbus_tcp.TcpMaster(host=HOST_Addr,port=HOST_Port)
    master.set_timeout(5.0)
    
    for i in range(14):
            clamp_data[i] = master.execute(1, cst.READ_HOLDING_REGISTERS, i*48, 48)
    
    
    for j in range(14):
        for i in range(24):
            data[j][i] = ReadFloat((clamp_data[0][i*2],clamp_data[0][i*2+1]))
    
    
    voltage01 = round(data[0][0],1)
    voltage02 = round(data[1][0],1)
    
    print (clamp_data[0][0])
    print (clamp_data[1])
    print (voltage01)
    print (voltage02)

'''
def getPowerLoop02(HOST_Addr, HOST_Port, voltage, pf):
    
    clamp32 = {}
    PowerPayload = {}
    clamp=[{"voltage":{}},{"voltage":{}},{"voltage":{}}]
    try:
        master = modbus_tcp.TcpMaster(host=HOST_Addr,port=HOST_Port)
        master.set_timeout(5.0)
        clamp_data = master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 54)
        #print (clamp_data)
        for i in range(27):
            clamp32[i] = ReadFloat((clamp_data[i*2+1], clamp_data[i*2]))
    
        for i in range(3):
            clamp[i]["voltage"]=voltage
            clamp[i]["current_r"]=clamp32[i*9]
            clamp[i]["current_s"]=clamp32[i*9+3]
            clamp[i]["current_t"]=clamp32[i*9+6]
            clamp[i]["temperature_r"]=clamp32[i*9+1]
            clamp[i]["temperature_s"]=clamp32[i*9+4]
            clamp[i]["temperature_t"]=clamp32[i*9+7]
            clamp[i]["battery_r"]=clamp32[i*9+2]
            clamp[i]["battery_s"]=clamp32[i*9+5]
            clamp[i]["battery_t"]=clamp32[i*9+8]
            clamp[i]["power"]= round((380*1.7*(clamp32[i*9]+clamp32[i*9+3]+clamp32[i*9+6]))/1000,1)
            clamp[i]["pf"]= pf
            clamp[i]["alive"]= 1
            payload_data = [{"values":clamp[i]}]
            
    except:
        for i in range(3):
            clamp[i]["voltage"]=i
            clamp[i]["current_r"]=i
            clamp[i]["current_s"]=i
            clamp[i]["current_t"]=i
            clamp[i]["temperature_r"]=i
            clamp[i]["temperature_s"]=i
            clamp[i]["temperature_t"]=i
            clamp[i]["battery_r"]=i
            clamp[i]["battery_s"]=i
            clamp[i]["battery_t"]=i
            clamp[i]["power"]= i
            clamp[i]["pf"]= i
            clamp[i]["alive"]= 2
            payload_data = [{"values":clamp[i]}]
    
    if clamp[1]["alive"] == 1 :
        clamp[1]["current_r"]=clamp[1]["current_r"]-clamp[2]["current_r"]
        clamp[1]["current_s"]=clamp[1]["current_s"]-clamp[2]["current_s"]
        clamp[1]["current_t"]=clamp[1]["current_t"]-clamp[2]["current_t"]
        clamp[1]["power"]= clamp[1]["power"]-clamp[2]["power"]
    
    with open('static/data/PowerLoop02.json', 'r') as f:
        power_kwh02 = json.load(f)
    f.close
    clamp[0]["power_kwh"] = power_kwh02["power06_kwh"]
    clamp[1]["power_kwh"] = power_kwh02["power07_kwh"]
    clamp[2]["power_kwh"] = power_kwh02["power08_kwh"]
    clamp[0]["energy"] = power_kwh02["power06_kwh"]
    clamp[1]["energy"] = power_kwh02["power07_kwh"]
    clamp[2]["energy"] = power_kwh02["power08_kwh"]
    
    
    clamp[0]["Loop_name"] = "F4EL1_BackupPower"
    clamp[1]["Loop_name"] = "F4NL1_LightPower"
    clamp[2]["Loop_name"] = "F4NR1_SocketPower"
    
    PowerPayload[0] = [{"access_token": "W8tpPG6jB0Ju3ogOxQoQ",
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[0]}]}]
    PowerPayload[1] = [{"access_token": "Zl0fvlfa7ZJAo8cX7RvO",
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[1]}]}]
    PowerPayload[2] = [{"access_token": "T6bEocUJOy7xaCyR0z62",
             "app": "ems_demo_fet",
             "type": "3P3WMETER",
             "data": [{"values":clamp[2]}]}]

    
    with open('static/data/PowerSubLoop08.json', 'w') as f:
        json.dump(PowerPayload[0][0]["data"][0]["values"], f)
    f.close
    
    with open('static/data/PowerSubLoop07.json', 'w') as f:
        json.dump(PowerPayload[1][0]["data"][0]["values"], f)
    f.close
    
    with open('static/data/PowerSubLoop06.json', 'w') as f:
        json.dump(PowerPayload[2][0]["data"][0]["values"], f)
    f.close


    return PowerPayload
    
def CleanPowerFlag():
    with open('static/data/PowerLoop01.json', 'r') as f:
        Power_data = json.load(f)
    Power_data["Power_Flag"] = 0
    with open('static/data/PowerLoop01.json', 'w') as g:
        json.dump(Power_data, g)
    f.close
    
    
def power_count():
    power_kwh01 = {}
    power_kwh02 = {}
    powermeter01 = (getPowerLoop01('192.168.1.10',502,380,0.9))
    
    
    with open('static/data/PowerLoop01.json', 'r') as f:
        power_kwh01 = json.load(f)
    f.close
    power_kwh01["power03_kwh"]=power_kwh01["power03_kwh"] + (powermeter01[0][0]["data"][0]["values"]["power"]/240)
    power_kwh01["power04_kwh"]=power_kwh01["power04_kwh"] + (powermeter01[1][0]["data"][0]["values"]["power"]/240)
    power_kwh01["power05_kwh"]=power_kwh01["power05_kwh"] + (powermeter01[2][0]["data"][0]["values"]["power"]/240)
    
    with open('static/data/PowerLoop01.json', 'w') as g:
        json.dump(power_kwh01, g)
    g.close
    
    
    powermeter02 = (getPowerLoop02('192.168.1.11',502,380,0.9))
    
    with open('static/data/PowerLoop02.json', 'r') as f:
        power_kwh02 = json.load(f)
    f.close
    power_kwh02["power06_kwh"]=power_kwh02["power06_kwh"] + (powermeter02[0][0]["data"][0]["values"]["power"]/240)
    power_kwh02["power07_kwh"]=power_kwh02["power07_kwh"] + (powermeter02[1][0]["data"][0]["values"]["power"]/240)
    power_kwh02["power08_kwh"]=power_kwh02["power08_kwh"] + (powermeter02[2][0]["data"][0]["values"]["power"]/240)
    with open('static/data/PowerLoop02.json', 'w') as g:
        json.dump(power_kwh02, g)
    g.close
'''    
    
if __name__ == '__main__':
    #print (getmodbustcp('192.5.1.120',502))
    print (getPowerLoop01('192.5.1.120',502))
    print (getPowerMainLoop01('192.5.1.120',502))
    print (GetPowerEnergy('192.5.1.120',502))
