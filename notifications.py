#Get's notification messages from user's database.

import requests

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

username = input('Enter your username: \n')

ahead = True
userId = notifyId(username)
noti_user = 'https://notify.moe/api/usernotifications/'
noti = 'https://notify.moe/api/notification/'
Id = []
msg = []

while ahead:
    get_noti = requests.get(noti_user + userId).json()
    noofid = len(get_noti['items'])

    for a in range(noofid):
        Id.append(get_noti['items'][a])
    
    for b in range(noofid):
        noti_url = requests.get(noti + Id[b]).json()
        msg.append(noti_url['message'])

    refresh = open('msgs.txt','w')
    refresh.write('Username: ' + username + '\nUserId: ' + userId + '\n' + '--NOTIFICATIONS-- \n\n')
    refresh.close()

    notify = open('msgs.txt','a')

    for b in range(noofid):
        notify.write('NotificationId: \'' + str(Id[b]) + '\'\nMessage: \'' + str(msg[b]) + '\'\n\n' )
        
    notify.close()
