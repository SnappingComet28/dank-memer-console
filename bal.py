'THIS PROGRAM WAS WRITTEN BEFORE I DECIDED TO ARRANGE THE CODE'

'IMPORTS'
import json

data = {}

'DISPLAYS USER\'S MONI'
def bal():
    try:
        with open("data/bal.json") as file:
           data = json.load(file)
        print("Your Monis:\n")
        for key,value in data.items(): 
            if key == "capacity":
                print(f"\t\t{value}")
                continue
            if key == "bank":
                print(f"\t{key}:\n\t\t{value}")
                continue
            print(f"\t{key}:\n\t\t{value}\n") 
        return
    except:
        return ("Not found",0)
    
'WITHRAWAL OF MONI FROM BANK'    
def withraw(amt):
    '''LOADING OF CURRENT BALANCE'''
    with open("data/bal.json") as file:
        data = json.load(file)
    
        '''REPLACEMENT OF ABBREVIATIONS IN ARGS'''
    if amt == "all":
        amt = data["bank"]
    elif "m" in amt:
        amt = int(amt.replace("m","000000"))
    elif "k" in amt:
        amt = int(amt.replace("k","000"))
    elif "b" in amt:
        amt = int(amt.replace("b","000000000"))
    else:
        try:
            amt = int((amt))
        except ValueError:
            print("is that a new unit like u (useless) lol")
            return
    
    '''CHECK IF BANK HAVE THAT MONEY'''
    if int(int(amt)) > data["bank"]:
        print("U tryna escape the matrix? how u withrawing that much if u dont have that much? broke nigga")
        return
    else:pass

    '''WITHRAWAL PROCESS'''
    data["bank"] = data["bank"]-amt
    data["pocket"] = data["pocket"]+amt
    with open("data/bal.json","wt") as file:
        json.dump(
            {
                "pocket":int(data["pocket"]),
                "bank":int(data["bank"]),
                "capacity":int(data["capacity"])
            }
            ,file,indent=4)
        print(f"done bro! now u have {data["pocket"]} money in ur pocket\nand {data["bank"]}/{data["capacity"]} in ur bank")
        return True
    
'DEPOSITION OF MONI TO BANK'
def deposit(amt):

    '''LOADING OF CURRENT BALANCE'''
    with open("data/bal.json") as file:
        data = json.load(file)
    
        '''REPLACEMENT OF ABBREVIATIONS IN ARGS'''
    if amt == "all":
        amt = data["pocket"]
    elif "m" in amt:
        amt = int(amt.replace("m","000000"))
    elif "k" in amt:
        amt = int(amt.replace("k","000"))
    elif "b" in amt:
        amt = int(amt.replace("b","000000000"))
    else:
        try:
            amt = int((amt))
        except ValueError:
            print("is that a new unit like u (useless) lol")
            return
    
    '''CHECK IF USER HAVE THAT MONEY'''
    if int(int(amt)) > data["pocket"]:
        print("U tryna escape the matrix? how u depositing that much if u dont have that much? broke nigga")
        return
    else:pass

    '''CHECK IF BANK CAN HOLD THAT MUCH'''
    if int(amt)+data["bank"] <= data["capacity"]:
        data["pocket"] = data["pocket"]-int(amt)
        data["bank"] = data["bank"]+int(amt)
        # try:
        '''DEPOSITION PROCESS'''
        with open("data/bal.json","wt") as file:
            json.dump(
                {
                    "pocket":int(data["pocket"]),
                    "bank":int(data["bank"]),
                    "capacity":int(data["capacity"])
                }
                ,file,indent=4)
            print(f"done bro! now u have {data["pocket"]} money in ur pocket\nand {data["bank"]}/{data["capacity"]} in ur bank")
            return True
        # except:
        #     return False
    else:
        if data["bank"] == data["capacity"]:
            print("the bank is full where will i put it? keep it in ur pocket")
            return
        amt =  data["capacity"] - data["bank"]
        data["pocket"] = data["pocket"]-int(amt)
        data["bank"] = data["bank"]+int(amt)
        # try:
        '''DEPOSITION PROCESS'''
        with open("data/bal.json","wt") as file:
            json.dump(
                {
                    "pocket":int(data["pocket"]),
                    "bank":int(data["bank"]),
                    "capacity":int(data["capacity"])
                }
                ,file,indent=4)
            print(f"done bro! now u have {data["pocket"]} money in ur pocket\nand {data["bank"]}/{data["capacity"]} in ur bank (bank full so i only put {amt})")
            return True
        
'ADMIN: ADD MONI'
def add(amount,of="pocket"):
    '''OPENING THE FILE IN BOTH READ AND WRITE'''
    amt = int(amount)
    with open("data/bal.json","rt") as fiel:
        '''GETTING LATEST DATA'''
        data = json.load(fiel)
    with open("data/bal.json","wt") as file:
        if of == "pocket":
            '''ADDITION OF MONI INTO POCKET'''
            data["pocket"] +=amt
            json.dump(data,file)
            print(f"now u have {data["pocket"]-amt} + {amt} = {data["pocket"]} moni in pocket")
            return True
        
        elif of == "capacity":
            data["capacity"] += amt
            json.dump(data,file)
            print(f"now u have {data["capacity"]-amt} + {amt} = {data["capacity"]}")
            return True
        else:
            return False

'ADMIN: SUBTRACT OF MONI'         
def subtract(amount,all=False):
    
    '''OPENING THE FILE IN BOTH READ AND WRITE'''
    amt = int(amount)
    with open("data/bal.json","rt") as fiel:
        '''GETTING LATEST DATA'''
        data = json.load(fiel)
    with open("data/bal.json","wt") as file:
        if not all:
            '''SUBTRACTION OF MONI FROM POCKET'''
            data["pocket"] -=amt
            if data["pocket"] < 0:
                print(f"lol imagine being in debt of {data["pocket"]}")
            json.dump(data,file)
            
            print(f"now u have {data["pocket"]+amt} - {amt} = {data["pocket"]} moni in pocket")
            return True
        
        elif all:
            '''SUBTRACTION OF ALL MONEY FROM POCKET'''
            data["pocket"] = 0 
            if data["pocket"] < 0:
                print(f"lol imagine being broke")
            json.dump(data,file)
            return True
        
        else:
            return False 