#   Date:        2022/04/27
#   Author:      Emma Gillespie
#   Description: A script that gets status of the server

#!/usr/bin/python3

def getLinuxStatus():
    statusData = {}

    # Computer upload and download speed
    with open('/proc/net/dev', 'r') as f:
        for line in f:
            if 'eth0' in line:
                download = line.split()[1]
                upload = line.split()[9]

                download = int(download) / 1024 / 1024
                upload = int(upload) / 1024 / 1024

                statusData['download'] = download
                statusData['upload'] = upload
    
    # Computer uptime
    with open('/proc/uptime', 'r') as f:
        uptime = f.readline().split()[0]

        days = int(uptime) // 86400
        hours = int(uptime) // 3600 % 24
        minutes = int(uptime) // 60 % 60

        statusData['uptime'] = days, hours, minutes
    
    # Computer memory usage
    with open('/proc/meminfo', 'r') as f:
        for line in f:
            if 'MemTotal' in line:
                memTotal = line.split()[1]
            if 'MemFree' in line:
                memFree = line.split()[1]
            if 'Buffers' in line:
                buffers = line.split()[1]
            if 'Cached' in line:
                cached = line.split()[1]

        memTotal = int(memTotal) / 1024
        memFree = int(memFree) / 1024
        buffers = int(buffers) / 1024
        cached = int(cached) / 1024

        statusData['memTotal'] = memTotal
        statusData['memFree'] = memFree
        statusData['buffers'] = buffers
        statusData['cached'] = cached
    
    # Computer CPU usage
    with open('/proc/stat', 'r') as f:
        for line in f:
            if 'cpu' in line:
                cpu = line.split()[1]

        cpu = int(cpu) / 100

        statusData['cpu'] = cpu

    return statusData
