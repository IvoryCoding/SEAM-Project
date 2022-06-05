#   Date:        2022/04/27
#   Author:      Emma Gillespie
#   Description: A script that post the json data to the server

#!/usr/bin/python3

import requests
import json

def postJSON(jsonData):
    newHeaders = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    
    r = requests.post('http://127.0.0.1:5000/post_json', jsonData, headers=newHeaders)

    if r.status_code == 200:
        print("\n\t\t[+] POST request successful!")
        print(f"\n\t\tStatus Code: {r.status_code} Response: \n{r.text}")
    else:
        print("\n\t\t[-] POST request failed!")