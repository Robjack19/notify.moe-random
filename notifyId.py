#extracting Notify userId

import requests 

def notifyId(username):
    url = 'https://notify.moe/api/nicktouser/'

    #checking if username is valid
   
    try:
        req = requests.get(url + username).json()
        userId = (req['userId'])
        return userId

    except:
        userId = 'null'
        return userId

username = input('Enter yout username: \n')
userId = notifyId(username)
ahead = True

if userId == 'null':
    print('Something went wrong: \n')
    ahead = False

while ahead:
    print('Your userId is: ' + userId)
    