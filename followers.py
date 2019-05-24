#gets name and id's of your followers

import requests

def get_name(ids):
    nick_url= 'https://notify.moe/api/user/'
    get_info = requests.get(nick_url + ids).json()
    nick = get_info['nick']
    return nick

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

aurl = 'https://notify.moe/api/animelist/'
username = input('Enter your username: \n')

ahead = True
userId = notifyId(username)

if userId is 'null':
    print('Invalid username or unknown error: \n')
    ahead = False

get_ids = 'https://notify.moe/api/userfollows/'

while ahead:
    request = requests.get(get_ids + userId).json()

    lent = len(request['items'])

    print('YOUR FOLLOWERS ARE: \n')

    for i in range(lent):

        ids = ''
        name = ''

        ids = (request['items'][i])
        print('ID: ' + ids )

        name = get_name(ids)
        print('NICK: ' + name + '\n')    

    print('--DONE--') 

    break