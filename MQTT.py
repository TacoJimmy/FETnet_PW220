# coding:utf-8
import codecs
import json
import ssl
import csv
import time

def save_csv():
    
    with open('static/data/PowerSubLoop01.json', 'r') as a:
        subpower01 = json.load(a)
    a.close
    
    with open('static/data/PowerSubLoop01.csv', 'a', newline="") as csvfile:
        json.dump(subpower01, csvfile)
    csvfile.close

if __name__ == '__main__':
    while True:
        save_csv()
        print("ok")
        time.sleep(5)