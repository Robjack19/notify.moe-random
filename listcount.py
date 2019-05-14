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

aurl = 'https://notify.moe/api/animelist/'
username = input('Enter your username: \n')

ahead = True
userId = notifyId(username)

if userId is 'null':
    print('Invalid username or unknown error: \n')
    ahead = False

status = []

watching = 0
planned = 0
completed = 0
hold = 0
dropped = 0

while ahead:
    lists = requests.get(aurl + userId).json()
    lent = len(lists['items'])

    for a in range(lent):
        status.append(lists['items'][a]['status'])

    for b in range(lent):
        
        if status[b] == 'watching':
            watching += 1

        elif status[b] == 'planned':
            planned += 1

        elif status[b] == 'completed':
            completed +=1

        elif status[b] == 'hold':
            hold += 1

        elif status[b] == 'dropped':
            dropped += 1
        
    print('--YOU ANIME LIST STATUS--\n')
    print('Total number of anime: ' + str(lent))
    print('Watching: ' + str(watching))
    print('Planned: ' + str(planned))
    print('Completed: ' + str(completed))
    print('On-Hold: ' + str(hold))
    print('Dropped: ' + str(dropped))

    break