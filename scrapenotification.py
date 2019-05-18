#gets users notification every hour(time can be changed)

import requests
import time

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

aurl = 'https://notify.moe/api/usernotifications/'
getnot = 'https://notify.moe/api/notification/'
ahead = True
times = False

username = input('Enter your username: \n')
userId = notifyId(username)

noyificationId = ''
check = 0

if userId is 'null':
    print('Invalid username or unknown error: \n')
    ahead = False

while ahead:
    notify = requests.get(aurl + userId).json()
    lent = len(notify['items']) - 1
    times = True
    break

while times:
    #ADJUST TIME IN SECONDS

    time.sleep(3600)
    notify2 = requests.get(aurl + userId).json()
    check = len(notify2['items']) - 1
    if check > lent:
        diff = check - lent
        a = 0
        b = lent 
        
        for a in range(diff):
            b += 1
        
            notificationId = notify2['items'][b]

            notification = requests.get(getnot + notificationId).json()

            print('Title: ' + notification['title'])
            print('Message: ' + notification['message'] + '\n')
        
    lent = check
