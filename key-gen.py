#   Date:        2022/04/27
#   Author:      Emma Gillespie
#   Description: A script that gets linux server information and sends it to webserver in the form of json

#!/usr/bin/python3

import string
import random

def genKeys():
    chars = string.ascii_lowercase + string.digits

    key = ''.join(random.choice(chars) for _ in range(15))
    return key

def saveKeys(key):
    file = open("gen-keys-ServerStat.txt", "a")
    file.write(f"{key}\n")

if __name__ == "__main__":
    print("Generating 20 keys....")

    for _ in range(20):
        key = genKeys()
        print(f"\t\t{key}")

        saveKeys(key)
    print("Done creating keys....")