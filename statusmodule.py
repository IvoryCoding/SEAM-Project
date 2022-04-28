#   Date:        2022/04/27
#   Author:      Emma Gillespie
#   Description: A script that gets status of the server

#!/usr/bin/python3

import psutil
import time

def getLinuxStatus():
    statusData = {}

    # Memory usage
    memTotal = psutil.virtual_memory().total / 1024 / 1024
    memUsed = psutil.virtual_memory().used / 1024 / 1024
    memFree = psutil.virtual_memory().free / 1024 / 1024

    statusData['memTotal'] = memTotal
    statusData['memFree'] = memFree
    statusData['memUsed'] = memUsed

    # CPU usage
    cpu = psutil.cpu_percent()
    cpu = int(cpu) / 100

    statusData['cpu'] = cpu

    # Disk usage
    disk = psutil.disk_usage('/')
    diskTotal = disk.total / 1024 / 1024
    diskUsed = disk.used / 1024 / 1024
    diskFree = disk.free / 1024 / 1024

    statusData['diskTotal'] = diskTotal
    statusData['diskUsed'] = diskUsed
    statusData['diskFree'] = diskFree

    # Network usage
    net = psutil.net_io_counters()
    netSent = net.bytes_sent / 1024 / 1024
    netRecv = net.bytes_recv / 1024 / 1024

    statusData['netSent'] = netSent
    statusData['netRecv'] = netRecv

    print("\n\t\t[+] Status module task complete. Sening data to server...")
    return statusData
