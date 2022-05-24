import time
import json
import requests

def invnewuser(i):
    while i==0:
        #делаем запрос к медоту
        r = requests.post('https://api.vk.com/method/groups.getRequests?group_id=(id группы вк)&access_token=(токен вк)&v=5.131')
        #читаем json
        item = json.loads(r.text)
        #число юзеров
        countinvite = item['response']['count']
        print('Всего зявок в группу: ' + str(countinvite))
        #если юзеров 0,то
        if countinvite == 0:
            print('Заявок нет')
        else:
            for ids in item['response']['items']:
                #тут наверно понятно
                idds = ids
                print('ID: ' + str(idds))
                #надоело писать коментарии))
                ri = requests.post('https://api.vk.com/method/groups.approveRequest?group_id=(id группы вк)&user_id='+str(idds) +'&access_token=(токен вк)&v=5.131')
                itemtwo = json.loads(ri.text)
                print(itemtwo)
        time.sleep(5)

invnewuser(0)