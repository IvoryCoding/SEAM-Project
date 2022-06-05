#   Date:        2022/04/27
#   Author:      Emma Gillespie
#   Description: A script that gets linux server information and sends it to webserver in the form of json

#!/usr/bin/python3

# Imports
from threading import *
import json
import time

# Program modules to import
import processmodule
import statusmodule
import networkmodule
import datamodule

serverIp = "192.168.1.178"

def processModule():
    try:
        with open('server-proc.json', 'w', encoding='utf-8') as f:
            json.dump(processmodule.getProcess(), f, ensure_ascii=False, indent=4)
    except:
        print("\n\t\t[!] Process module failed\n")

def statusModule():
    try:
        with open("server-status.json", "w", encoding="utf-8") as f:
            json.dump(statusmodule.getLinuxStatus(), f, ensure_ascii=False, indent=4)
    except:
        print("\n\t\t[!] Status module failed\n")

def networkModule():
    try:
        with open("server-net.json", "w", encoding="utf-8") as f:
            json.dump(networkmodule.getOpenPorts(serverIp), f, ensure_ascii=False, indent=4)
    except:
        print("\n\t\t[!] Network module failed\n")

if __name__ == "__main__":
    while True:

        print('\n\t\t' + '-' * 60)

        threadList = []

        # Create threads to run modules
        pmThread = Thread(target=processModule)
        ssmThread = Thread(target=statusModule)
        nmThread = Thread(target=networkModule)

        threadList.append(pmThread)
        threadList.append(ssmThread)
        threadList.append(nmThread)

        for x in threadList:
            x.start()

        for x in threadList:
            x.join()

        try:
            with open('server-proc.json', 'r', encoding='utf-8') as f:
                procData = json.load(f)
            with open('server-status.json', 'r', encoding='utf-8') as f:
                statusData = json.load(f)
            with open('server-net.json', 'r', encoding='utf-8') as f:
                netData = json.load(f)

            data = {'server': serverIp, 'process': procData, 'status': statusData, 'network': netData}
            jsonData = json.dumps(data)

            datamodule.postJSON(jsonData)
        except:
            print("\n\t\t[!] Error posting data\n")

        time.sleep(5)
