#   Date:        2022/04/27
#   Author:      Emma Gillespie
#   Description: A script that gets status of the server

#!/usr/bin/python3

# Imports
import socket
import threading
#import whatismyip

openPorts = {}

def tryPorts(ip, port):
    # Connect to the port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.AF_INET, socket.SOCK_STREAM
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(3)
    result = sock.connect_ex((ip, port))

    try:
        banner = sock.recv(1024).decode('utf-8')
    except:
        banner = 'No banner'

    if result == 0:
        openPorts[port] = banner
    
    sock.close()

# Gets open ports on current machine
def getOpenPorts():
    #IP address of current machine
    #ip = whatismyip.whatismyipv4()
    ip = '192.168.1.81'

    for port in range(0, 1024):
        thread = threading.Thread(target=tryPorts, args=(ip, port))
        thread.start()
    
    print("\n\t\t[+] Network module task complete. Sening data to server...")
    return openPorts

# Vuln checker and connections to machine???