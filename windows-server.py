#   Date:        2022/04/27
#   Author:      Emma Gillespie
#   Description: A script that gets windows server information and sends it to webserver in the form of json
#   Resources:

#!/usr/bin/python3

import json
import processmodule

def processModule():
        with open('server-proc.json', 'w', encoding='utf-8') as f:
                json.dump(processmodule.getProcess(), f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
        processModule()
