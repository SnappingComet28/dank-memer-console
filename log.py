'THIS PROGRAM WAS WRITTEN BEFORE I DECIDED TO ARRANGE THE CODE'

import json
def logcheck():
    try:
        with open("./data/user.json") as file:
            data = json.load(file)
            if data:
                return data["name"]
            else:
                return False 
    except FileNotFoundError:
        return False
def login(user):
    try:
        with open("./data/user.json",'wt+') as file:
            json.dump({"name":user})
            if json.load(file):
                return True
            else:
                return False
    except:
        return False
        
    
if __name__=="__main__":
    print(logcheck())              