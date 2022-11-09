# coding:utf-8
import codecs
from flask import Flask, render_template, request, jsonify, json
import schedule  
import time  
from flask import Flask
from flask_apscheduler import APScheduler
import FET_MQTT
import FET_modbustcp
from livereload import Server
import time
import csv



app = Flask(__name__)


class Config(object):
    JOBS = [
        {
            'id': 'publish_PowerMeter',  
            'func': '__main__:publish_PowerMeter',
            'args': (1, 2),   
            'trigger': 'interval',
            'minutes': 2
            #'seconds': 10
            
        },
        {
            'id': 'read_com1',  
            'func': '__main__:read_com1',
            'args': (1, 2),   
            'trigger': 'interval',
            'minutes': 15
            #'seconds': 15 
            
        },
        {
            'id': 'save_data',  
            'func': '__main__:save_data',
            'args': (1, 2),   
            'trigger': 'interval',
            'minutes': 5
            
            
        }
    ]
    SCHEDULER_API_ENABLED = True

@app.route('/')
@app.route('/setup')
def webapi():
    return render_template('setup.html')


@app.route('/powermanage')
def powermanage():
    return render_template('powermanage.html')

@app.route('/powermanage/message', methods=['GET'])
def powermanageMessage():
    if request.method == "GET":
        with open('static/data/message.json', 'r') as f:
            data = json.load(f)
            print("text : ", data)
        f.close
        return jsonify(data)

@app.route('/powermanage/ipc', methods=['GET'])
def poweripc():
    if request.method == "GET":
        with open('static/data/ipc.json', 'r') as f:
            data = json.load(f)
            print("text : ", data)
        f.close
        return jsonify(data)

@app.route('/powermanage/mainloop01', methods=['GET'])
def powermainloop01():
    if request.method == "GET":
        with open('static/data/PowerMainLoop01.json', 'r') as f:
            data = json.load(f)
            #print("text : ", data)
        f.close
        return jsonify(data)
    
@app.route('/powermanage/mainloop02', methods=['GET'])
def powermainloop02():
    if request.method == "GET":
        with open('static/data/PowerMainLoop02.json', 'r') as f:
            data = json.load(f)
            #print("text : ", data)
        f.close
        return jsonify(data)
    
@app.route('/powermanage/subloop01', methods=['GET'])
def powersubloop01Message():
    if request.method == "GET":
        with open('static/data/PowerSubLoop01.json', 'r') as f:
            data = json.load(f)
        f.close
    return jsonify(data)
@app.route('/powermanage/subloop02', methods=['GET'])
def powersubloop02Message():
    if request.method == "GET":
        with open('static/data/PowerSubLoop02.json', 'r') as f:
            data = json.load(f)
        f.close
    return jsonify(data)
@app.route('/powermanage/subloop03', methods=['GET'])
def powersubloop03Message():
    if request.method == "GET":
        with open('static/data/PowerSubLoop03.json', 'r') as f:
            data = json.load(f)
        f.close
    return jsonify(data)
@app.route('/powermanage/subloop04', methods=['GET'])
def powersubloop04Message():
    if request.method == "GET":
        with open('static/data/PowerSubLoop04.json', 'r') as f:
            data = json.load(f)
        f.close
    return jsonify(data)
@app.route('/powermanage/subloop05', methods=['GET'])
def powersubloop05Message():
    if request.method == "GET":
        with open('static/data/PowerSubLoop05.json', 'r') as f:
            data = json.load(f)
        f.close
    return jsonify(data)
@app.route('/powermanage/subloop06', methods=['GET'])
def powersubloop06Message():
    if request.method == "GET":
        with open('static/data/PowerSubLoop06.json', 'r') as f:
            data = json.load(f)
        f.close
    return jsonify(data)
@app.route('/powermanage/subloop07', methods=['GET'])
def powersubloop07Message():
    if request.method == "GET":
        with open('static/data/PowerSubLoop07.json', 'r') as f:
            data = json.load(f)
        f.close
    return jsonify(data)
@app.route('/powermanage/subloop08', methods=['GET'])
def powersubloop08Message():
    if request.method == "GET":
        with open('static/data/PowerSubLoop08.json', 'r') as f:
            data = json.load(f)
        f.close
    return jsonify(data)

@app.route('/powermanage/subloop09', methods=['GET'])
def powersubloop09Message():
    if request.method == "GET":
        with open('static/data/PowerSubLoop09.json', 'r') as f:
            data = json.load(f)
        f.close
    return jsonify(data)
@app.route('/powermanage/subloop10', methods=['GET'])
def powersubloop10Message():
    if request.method == "GET":
        with open('static/data/PowerSubLoop10.json', 'r') as f:
            data = json.load(f)
        f.close
    return jsonify(data)
@app.route('/powermanage/subloop11', methods=['GET'])
def powersubloop11Message():
    if request.method == "GET":
        with open('static/data/PowerSubLoop11.json', 'r') as f:
            data = json.load(f)
        f.close
    return jsonify(data)
@app.route('/powermanage/subloop12', methods=['GET'])
def powersubloop12Message():
    if request.method == "GET":
        with open('static/data/PowerSubLoop12.json', 'r') as f:
            data = json.load(f)
        f.close
    return jsonify(data)
@app.route('/powermanage/subloop13', methods=['GET'])
def powersubloop13Message():
    if request.method == "GET":
        with open('static/data/PowerSubLoop13.json', 'r') as f:
            data = json.load(f)
        f.close
    return jsonify(data)
@app.route('/powermanage/subloop14', methods=['GET'])
def powersubloop14Message():
    if request.method == "GET":
        with open('static/data/PowerSubLoop14.json', 'r') as f:
            data = json.load(f)
        f.close
    return jsonify(data)


@app.route('/setup/message', methods=['GET'])
def getDataMessage():
    if request.method == "GET":
        with open('static/data/message.json', 'r') as f:
            data = json.load(f)
            print("text : ", data)
        f.close
        return jsonify(data)


@app.route('/setup/COM01', methods=['POST'])
def setDataCOM01():
    if request.method == "POST":
        data = {
            'appInfo': {
                'COM01_Status': request.form['COM01_Status'],
                'COM01_BaudRate': request.form['COM01_BaudRate'],
                'COM01_DataSize': request.form['COM01_DataSize'],
                'COM01_Parity': request.form['COM01_Parity'],
                'COM01_StopBits': request.form['COM01_StopBits'],
            }
        }
        print(type(data))
        with open('static/data/COM01.json', 'w') as f:
            json.dump(data, f)
        f.close
        return jsonify(result='OK')
    
@app.route('/setup/COM02', methods=['POST'])
def setDataCOM02():
    if request.method == "POST":
        data = {
            'appInfo': {
                'COM02_Status': request.form['COM02_Status'],
                'COM02_BaudRate': request.form['COM02_BaudRate'],
                'COM02_DataSize': request.form['COM02_DataSize'],
                'COM02_Parity': request.form['COM02_Parity'],
                'COM02_StopBits': request.form['COM02_StopBits'],
            }
        }
        print(type(data))
        with open('static/data/COM02.json', 'w') as f:
            json.dump(data, f)
        f.close
        return jsonify(result='OK')
    
@app.route('/setup/TCP01', methods=['POST'])
def setDataTCP01():
    if request.method == "POST":
        data = {
            'appInfo': {
                'TCP01_IP': request.form['TCP01_IP'],
                'TCP01_PORT': request.form['TCP01_PORT'],
            }
        }
        print(type(data))
        with open('static/data/TCP01.json', 'w') as f:
            json.dump(data, f)
        f.close
        return jsonify(result='OK')

@app.route('/setup/TCP02', methods=['POST'])
def setDataTCP02():
    if request.method == "POST":
        data = {
            'appInfo': {
                'TCP02_IP': request.form['TCP02_IP'],
                'TCP02_PORT': request.form['TCP02_PORT'],
            }
        }
        print(type(data))
        with open('static/data/TCP02.json', 'w') as f:
            json.dump(data, f)
        f.close
        return jsonify(result='OK')

@app.route('/setup/mqtt01', methods=['POST'])
def setDataMqtt01():
    if request.method == "POST":
        data = {
            'appInfo': {
                'MQTT_ClientID': request.form['MQTT_ClientID'],
                'MQTT_UserName': request.form['MQTT_UserName'],
                'MQTT_Password': request.form['MQTT_Password'],
                'MQTT_url': request.form['MQTT_url'],
                'MQTT_Port': request.form['MQTT_Port'],
                'MQTT_SSL': request.form['MQTT_SSL'],
            }
        }
        print(type(data))
        with open('static/data/mqtt01.json', 'w') as f:
            json.dump(data, f)
        f.close
        return jsonify(result='OK')

def publish_PowerMeter(a, b):
    
    FET_MQTT.MqttPublish()
    print("ok")
    
def read_com1(a, b):
    
    energy_now = FET_modbustcp.GetPowerEnergy('192.168.1.51',1502)
    
    with open('static/data/power_dm.json', 'r') as f:
        power_energy_last = json.load(f)
    f.close
    
    dm_now = energy_now - power_energy_last["power_energy"]
    Payload = {"power_energy":energy_now, "power_dm":dm_now}
    
    with open('static/data/power_dm.json', 'w') as f:
            json.dump(Payload, f)
    f.close

    return Payload

def save_data(a, b):

    datatime = time.strftime("%Y-%m-%d-%H:%M:%S")
    with open('static/data/PowerSubLoop01.json', 'r') as a:
        subpower01 = json.load(a)
        subpower01["datatime"] = str(datatime)
    a.close
    with open("/media/mmcblk0p1/"+time.strftime("%Y-%m-%d")+"-SubLoop01.csv", "a", newline="")as csvfile:
        csv.dump(subpower01, csvfile)
    csvfile.close
    
    with open('static/data/PowerSubLoop02.json', 'r') as a:
        subpower02 = json.load(a)
        csv.dump(subpower02, csvfile)
    a.close
    with open("/media/mmcblk0p1/"+time.strftime("%Y-%m-%d")+"-SubLoop02.csv", "a", newline="")as csvfile:
        csv.dump(subpower02, csvfile)
    csvfile.close

    with open('static/data/PowerSubLoop03.json', 'r') as a:
        subpower03 = json.load(a)
        subpower03["datatime"] = str(datatime)
    a.close
    with open("/media/mmcblk0p1/"+time.strftime("%Y-%m-%d")+"-SubLoop03.csv", "a", newline="")as csvfile:
        csv.dump(subpower03, csvfile)
    csvfile.close

    with open('static/data/PowerSubLoop04.json', 'r') as a:
        subpower04 = json.load(a)
        subpower04["datatime"] = str(datatime)
    a.close
    with open("/media/mmcblk0p1/"+time.strftime("%Y-%m-%d")+"-SubLoop04.csv", "a", newline="")as csvfile:
        csv.dump(subpower04, csvfile)
    csvfile.close

    with open('static/data/PowerSubLoop05.json', 'r') as a:
        subpower05 = json.load(a)
        subpower05["datatime"] = str(datatime)
    a.close
    with open("/media/mmcblk0p1/"+time.strftime("%Y-%m-%d")+"-SubLoop05.csv", "a", newline="")as csvfile:
        csv.dump(subpower05, csvfile)
    csvfile.close

    with open('static/data/PowerSubLoop06.json', 'r') as a:
        subpower06 = json.load(a)
        subpower06["datatime"] = str(datatime)
    a.close
    with open("/media/mmcblk0p1/"+time.strftime("%Y-%m-%d")+"-SubLoop06.csv", "a", newline="")as csvfile:
        csv.dump(subpower06, csvfile)
    csvfile.close

    with open('static/data/PowerSubLoop07.json', 'r') as a:
        subpower07 = json.load(a)
        subpower07["datatime"] = str(datatime)
    a.close
    with open("/media/mmcblk0p1/"+time.strftime("%Y-%m-%d")+"-SubLoop07.csv", "a", newline="")as csvfile:
        csv.dump(subpower07, csvfile)
    csvfile.close

    with open('static/data/PowerSubLoop08.json', 'r') as a:
        subpower08 = json.load(a)
        subpower08["datatime"] = str(datatime)
    a.close
    with open("/media/mmcblk0p1/"+time.strftime("%Y-%m-%d")+"-SubLoop08.csv", "a", newline="")as csvfile:
        csv.dump(subpower08, csvfile)
    csvfile.close

    with open('static/data/PowerSubLoop09.json', 'r') as a:
        subpower09 = json.load(a)
        subpower09["datatime"] = str(datatime)
    a.close
    with open("/media/mmcblk0p1/"+time.strftime("%Y-%m-%d")+"-SubLoop09.csv", "a", newline="")as csvfile:
        csv.dump(subpower09, csvfile)
    csvfile.close

    with open('static/data/PowerSubLoop10.json', 'r') as a:
        subpower10 = json.load(a)
        subpower10["datatime"] = str(datatime)
    a.close
    with open("/media/mmcblk0p1/"+time.strftime("%Y-%m-%d")+"-SubLoop10.csv", "a", newline="")as csvfile:
        csv.dump(subpower10, csvfile)
    csvfile.close

    with open('static/data/PowerSubLoop11.json', 'r') as a:
        subpower11 = json.load(a)
        subpower11["datatime"] = str(datatime)
    a.close
    with open("/media/mmcblk0p1/"+time.strftime("%Y-%m-%d")+"-SubLoop11.csv", "a", newline="")as csvfile:
        csv.dump(subpower11, csvfile)
    csvfile.close

    with open('static/data/PowerSubLoop12.json', 'r') as a:
        subpower12 = json.load(a)
        subpower12["datatime"] = str(datatime)
    a.close
    with open("/media/mmcblk0p1/"+time.strftime("%Y-%m-%d")+"-SubLoop12.csv", "a", newline="")as csvfile:
        csv.dump(subpower12, csvfile)
    csvfile.close

    with open('static/data/PowerSubLoop13.json', 'r') as a:
        subpower13 = json.load(a)
        subpower13["datatime"] = str(datatime)
    a.close
    with open("/media/mmcblk0p1/"+time.strftime("%Y-%m-%d")+"-SubLoop13.csv", "a", newline="")as csvfile:
        csv.dump(subpower13, csvfile)
    csvfile.close

    with open('static/data/PowerSubLoop14.json', 'r') as a:
        subpower14 = json.load(a)
        subpower14["datatime"] = str(datatime)
    a.close
    with open("/media/mmcblk0p1/"+time.strftime("%Y-%m-%d")+"-SubLoop14.csv", "a", newline="")as csvfile:
        csv.dump(subpower14, csvfile)
    csvfile.close


if __name__ == '__main__':
    
    app.config.from_object(Config())
    scheduler = APScheduler()
    scheduler.init_app(app) 
    scheduler.start()
    
    live_server = Server(app.wsgi_app)
    live_server.watch('static/*.stylus', 'make static')
    live_server.serve(open_url=False, open_url_delay=None, live_css=False, host='0.0.0.0', debug=None, restart_delay=100)
    
    