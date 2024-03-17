def logcheck():
    try:
        with open("data/user.txt") as file:
            data = file.read()
            if data:
                return data.replace("name:","")
            else:
                return False 
    except FileNotFoundError:
        return False
def login(user):
    try:
        with open("data/user.txt",'wt+') as file:
            file.write(f"name:{user}")
            if file.read():
                return True
            else:
                return False
    except:
        return False
        
    
                