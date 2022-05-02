#   Date:        2022/04/27
#   Author:      Emma Gillespie
#   Description: A script that post the json data to the server

#!/usr/bin/python3

import requests
import json

def postJSON(): # Add data parameter
    newHeaders = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    jsonInfo = {"Id": "1", "Name": "Emma", "Age": "21"}
    
    r = requests.post('http://127.0.0.1:5000/servers', jsonInfo, headers=newHeaders)

    print(f"\n\t\tStatus Code: {r.status_code} Response: \n{r.text}")