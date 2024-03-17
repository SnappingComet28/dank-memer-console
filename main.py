'''OTHER IMPORTS'''

'''DANK EXTENSIONS'''
import log 
import bal


'''
THIS PART CHECKS FOR LOGIN OF USER. IF NOT THEN CREATES AN ACCOUNT
'''
if not log.logcheck():
    print("\nWelcome user!\n\n")
    print("Please make an account by entering credentials")
    while True:
        name=input("Name pls\n$ ")
        if name:
            break
    if not log.login(name):
        print("Some error occured. Seeya later homie")
        exit(1)

else:
    user = log.logcheck()
'''
FIRE UP OF DANK MEMER TO THE USER AND ASKS FOR QUERY
''' 
print(f"Greetings {user}!",end="")
while True:
    query = input("\n$ ")

    '''COMMANDS AND QUERIES POSSIBLE'''
    if query == 'bal':
        '''CHECK FOR BALANCE'''
        if not bal.bal():
            print("Smt went wrong bruh im going")
            exit(0)
    
    elif "withraw" in query or "with" in query:
        if "withraw" in query:
            query = query.replace("withraw","").strip()
        else:
            query = query.replace("with","").strip()
        bal.withraw(query)

    elif "deposit" in query or "dep" in query:
        if "deposit" in query:
            query = query.replace("deposit","").strip()
        else:
            query = query.replace("dep","").strip()
        bal.deposit(query)

    elif query == 'bye':
        '''TERMINATION'''
        print(f"Cya later {user}!")
        break

    else:
        print("What are u doing nigga? write correctly")