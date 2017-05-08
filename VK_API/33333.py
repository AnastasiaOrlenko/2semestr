import requests
import json
import re
import sys

def vk_api(method, **kwargs):
    api_request = 'https://api.vk.com/method/'+method + '?'
    api_request += '&'.join(['{}={}'.format(key, kwargs[key]) for key in kwargs])
    return json.loads(requests.get(api_request).text)

def downloadingposts():
    group_info = vk_api('groups.getById', group_id='kino.culture', v='5.63')
    group_id = group_info['response'][0]['id']

    posts = []
    item_count = 150
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd) 

    result = vk_api('wall.get', owner_id=-group_id, v='5.63', count=100)
    posts += result["response"]["items"]
    while len(posts) < item_count:
        result = vk_api('wall.get', owner_id=-group_id, v='5.63', count=100, offset=len(posts))
        posts += result['response']["items"]
        for postik in posts:
            text = postik['text'].translate(non_bmp_map)
            new_posts = re.sub('http[^ ]*?($| |,)', '', text).replace('<br>', ' ')
            with open('posts.txt', 'a', encoding='utf-8') as posti:
                posti.write(str(postik['id']) + ' ' + new_posts + '\n')
            
    return posts, new_posts
    print(type(new_posts))
    
def comments(posts):
    group_info = vk_api('groups.getById', group_id='kino.culture', v='5.63')
    group_id = group_info['response'][0]['id']
    
    #id_polzovatelei = []
    #сюда добавить 
    
    comments = []
    item_count = 150
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    
    for postik in posts:
        result = vk_api('wall.getComments', owner_id=-group_id, post_id=postik['id'], v='5.63', count=100)
        comments += result["response"]["items"]
        for comment in comments:
            new_comments = comment['text'].translate(non_bmp_map)
            clean_comments = re.sub('\[.*?\]','', new_comments)
            with open('comments.txt', 'a', encoding='utf-8') as commenti:
                commenti.write(str(postik['id']) + ' ' + clean_comments + '\n')
    return clean_comments
    
    
def lenghtofposts(new_posts):
    regex = re.compile('[^а-яёА-ЯЁ0-9a-zA-Z]+', flags=re.U | re.DOTALL)
    new_posts = re.sub(regex, ' ', new_posts)
    words = new_posts.split(' ')
    lenght = len(words)
    #ниже просто проверка, после которой я поняла, что все сломалось(((
    file = open('lenght.txt', 'w', encoding='utf-8')
    file.write(str(lenght) + '\n')
    return lenght  
    
            
''' for postik in posts:
        idofuser = postik.get('id')
        commentss = vk_api('wall.getComments', owner_id=-group_id, count=100, post_id=idofuser)

        for comment in commentss['response'][1:]:
            idofuser = comment['from_id']
            idofuser = str(idofuser).replace('-', '')
            id_polzovatelei.append(idofuser)
            allid = str(idofuser) + '\n'

            with open('users.txt', 'a', encoding='utf-8') as idishki:
                    idishki.write(allid)
    return id_polzovatelei
'''    #id находит, но все тщетно с подсчетами длин комментов и постов, может просто голова уже не соображает
def main():

    posts, new_posts = downloadingposts()
    clean_comments = comments(posts)
    lenght = lenghtofposts(new_posts)
  

if __name__ == '__main__':
    main()






             
