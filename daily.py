from time import time
import bal
import json 
def check():
    now = time()
    with open("data/lastdaily.json") as file:
        data = json.load(file)
    last = data["lastdaily"]

    if round(now-last) >= 86400 and round(now-last) < 2*86400:
        ''' ADDS THE MONI'''
        bal.add((100000+1000*data["streak"]),of="pocket")
        with open("data/lastdaily.json","wt") as file1:
            json.dump({
                "lastdaily":now,
                "streak":data["streak"]+1
            },file1)
        print(f"done bro! ur daily streak is now {data["streak"]+1}")
        return True
    
    elif round(now-last) > 2*86400:
        ''' ADDS THE MONI'''
        with open("data/lastdaily.json","wt") as fiel:
            data["streak"] = 0
            json.dump(data,fiel)
        with open("data/lastdaily.json") as jdj:
            data = json.load(jdj)
        bal.add(100000+1000*data["streak"],of="pocket")
        with open("data/lastdaily.json","wt") as file1:
            json.dump({
                "lastdaily":now,
                "streak":data["streak"]+1
            },file1)
        print(f"done bro! ur daily streak is now {data["streak"]+1}")
        return True
    
    elif round(now-last) < 86400:
        '''SAYS TO RETURN AFTER TIME FOR THE MONI'''
        print(f"ur too fast just return after {round((86400-(now-last))/3600)}hrs for moni")
        return True
    else:
        return False    