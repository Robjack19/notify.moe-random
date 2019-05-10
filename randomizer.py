#Selects a random anime from your 'planned' list.

import requests
from random import randint
import webbrowser

aurl = 'https://notify.moe/api/animelist/'
username = input('Enter your username: \n')

def notifyId(username):
    url = 'https://notify.moe/api/nicktouser/'

    #checking if username is valid
   
    try:
        req = requests.get(url + str(username)).json()
        userId = (req['userId'])
        return userId

    except:
        userId = 'null'
        return userId

ahead = True
userId = notifyId(username)

nanimeId = []
watching = []
status = ''

if userId is 'null':
    print('Invalid username or unknown error: \n')
    ahead = False

while ahead:
    getlist = requests.get(aurl + userId).json()
    noofanime  = len(getlist['items'])

    for a in range(noofanime):
        status = (getlist['items'][a]['status'])

        if status == 'planned':
            nanimeId.append(getlist['items'][a]['animeId'])

    size = len(nanimeId)

    rand = randint(0, size)
    anime = nanimeId[rand]

    new = 2
    link = 'https://notify.moe/anime/'
    alink = link + str(anime)
    webbrowser.open(alink,new = new)
    
    break