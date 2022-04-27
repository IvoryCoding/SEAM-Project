#   Date:        2022/04/27
#   Author:      Emma Gillespie
#   Description: A script that gets linux server information and sends it to webserver in the form of json

#!/usr/bin/python3

from threading import *
import json

# Modules to import
import processmodule
import statusmodule

def processModule():
    try:
        with open('server-proc.json', 'w', encoding='utf-8') as f:
            json.dump(processmodule.getProcess(), f, ensure_ascii=False, indent=4)
    except:
        print("Process module failed")

def serverStatusModule():
    try:
        with open("server-status.json", "w", encoding="utf-8") as f:
            json.dump(statusmodule.getLinuxStatus(), f, ensure_ascii=False, indent=4)
    except:
        print("Status module failed")

if __name__ == "__main__":
    # Create threads to run modules
    pmThread = Thread(target=processModule)
    pmThread.start()

    ssmThread = Thread(target=serverStatusModule)
    ssmThread.start()
