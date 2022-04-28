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
            json.dump(networkmodule.getOpenPorts(), f, ensure_ascii=False, indent=4)
    except:
        print("\n\t\t[!] Network module failed\n")

if __name__ == "__main__":
    while True:
        # Create threads to run modules
        pmThread = Thread(target=processModule)
        pmThread.start()

        ssmThread = Thread(target=statusModule)
        ssmThread.start()

        # Need to make the script much faster
        nmThread = Thread(target=networkModule)
        nmThread.start()

        time.sleep(60)
