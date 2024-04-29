'THIS PROGRAM WAS WRITTEN BEFORE I DECIDED TO ARRANGE THE CODE'

'IMPORTS'
from time import time
import bal
import json

'CHECKS THE LAST "DAILY" RAN'
def check():
    'RECORDS CURRENT TIME'
    now = time()
    
    'OPENS THE RECORD TO GET THE TIME OF LAST "DAILY" RAN'
    with open("./data/lastdaily.json") as file:
        data = json.load(file)
    last = data["lastdaily"]

    #'IF DAILY WAS RAN WITHIN 48 HRS'
    if round(now-last) >= 86400 and round(now-last) < 2*86400:
        ''' ADDS THE MONI'''
        bal.add((100000+1000*data["streak"]),of="pocket")
        with open("./data/lastdaily.json","wt") as file1:
            json.dump({
                "lastdaily":now,
                "streak":data["streak"]+1
            },file1)
        print(f"done bro! ur daily streak is now {data["streak"]+1}")
        return True
    
    #'IF THE DAILY WAS RAN AFTER 48 HRS'
    elif round(now-last) > 2*86400:
        ''' ADDS THE MONI'''
        with open("./data/lastdaily.json","wt") as fiel:
            data["streak"] = 0
            json.dump(data,fiel)
        with open("./data/lastdaily.json") as jdj:
            data = json.load(jdj)
        bal.add(100000+1000*data["streak"],of="pocket")
        with open("./data/lastdaily.json","wt") as file1:
            json.dump({
                "lastdaily":now,
                "streak":data["streak"]+1
            },file1)
        print(f"wow! u lost ur streak and ur daily streak is now {data["streak"]+1}")
        return True
    #'IF DAILY WAS RAN WITHIN 24 HRS'
    elif round(now-last) < 86400:
        '''SAYS TO RETURN AFTER TIME FOR THE MONI'''
        print(f"ur too fast just return after {round((86400-(now-last))/3600)}hrs for moni")
        return True    