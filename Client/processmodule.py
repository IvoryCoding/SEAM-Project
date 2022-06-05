#   Date:        2022/04/27
#   Author:      Emma Gillespie
#   Description: A script that gets process details of server
#   Resources:

#!/usr/bin/python3

import psutil
import time

def getProcess():
    listOfPrcesses = list()
    processDict = dict()

    for proc in psutil.process_iter():
        procDict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent'])
        procDict['vms'] = proc.memory_info().vms / (1024 * 1024)
        listOfPrcesses.append(procDict)

    listOfPrcesses = sorted(listOfPrcesses, key=lambda procObj: procObj['vms'], reverse=True)

    for proc in listOfPrcesses:
        processDict[proc['name']] = proc

    print("\n\t\t[+] Process module task complete. Sening data to server...")
    return processDict