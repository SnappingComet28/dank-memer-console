import json
data = {}
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
        return True
    except:
        return False #not found
def withraw(amt):
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
        return True
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
            return True
        # except:
        #     return False
    else:
        print("Bank can't have that much moni, keep it in ur pocket")    
    