import urllib.request 
import os
import re

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        text = page.read().decode('utf-8')
    except:
        print('Error at', pageUrl)
        return links.append(pageUrl)

commonUrl = 'http://gazeta-bam.ru/article/'
for i in range(1227, 115223):
    pageUrl = commonUrl + str(i)
    download_page(pageUrl)

def stranica(pageUrl):
    req = urllib.request.Request(pageUrl) 
    with urllib.request.urlopen(req) as response: 
        html = response.read().decode('utf-8')
    return(html)

def article(html):
    regPostTitle = re.compile('<div class=".+?Категории:</h3><ul><li><a href=".+?>.+?<h2 class="b-object__detail__share__title">', flags=re.U | re.DOTALL) 
    titles = regPostTitle.findall(html) 

    new_titles = [] 
    regTag = re.compile('<.*?>', flags=re.U | re.DOTALL) 
    regSpace = re.compile('\s{2,}', flags=re.U | re.DOTALL) 
    for t in titles: 
        clean_t = regSpace.sub("", t) 
        clean_t = regTag.sub("", clean_t) 
        new_titles.append(clean_t) 
        for t in new_titles: 
            print(t)
    return(html)
        
def get_date(html):
    regdate = re.compile('<span class="b-object__detail__issue__date">([0-9]{1,2})[.]([0-9]{1,2})[.]([0-9]{4})</span>', flags=re.U | re.DOTALL)
    regexdate = re.search(regdate, html)
    if regexdate:
        date = regexdate.group(1)
        month = regexdate.group(2)
        year = regexdate.group(3)
    else:
        date = 'nodate'
        month = 'nomonth'
        year = 'noyear'
    return (date, month, year)

def get_header(html):
    regheader = re.compile('<a href=".+?>(.+?)</a>', flags=re.U | re.DOTALL)
    regexheader = re.search(regheader, html)
    if regexheader:
        header = regexheader.group(1)
    else:
        header = 'noheader'
    return (header)

def get_topic(html):
    regtopic = re.compile('<div class=".+?Категории:</h3><ul><li><a href=".+?>(.+?)</a></li></ul></div>', flags=re.U | re.DOTALL)
    regextopic = re.search(regtopic, html)
    if regextopic:
        topic = regextopic.group(1)
    else:
        topic = 'notopic'
    return (topic)

author = 'noname'

def metadata(path, author, header, artname, date, topic, link, year):
    row = 'http://gazeta-bam.ru/article/115223/'
    path = path + os.sep + artname + '.txt'
    filee = open('/Users/pettishin/Desktop/' + os.sep + 'MestnoeVremya' + os.sep + 'metadata.csv', 'w', encoding = 'utf-8')
    filee.write(row % ('path', 'author', 'header', 'date', 'topic', 'link', 'year'))
    filee.close()

def main():
    stranica(pageUrl)
    html = stranica(pageUrl)
    html = article(html)
    date, month, year = get_date(html)
    header = get_header(html)
    topic = get_topic(html)
    metadata(path, author, header, artname, date, topic, link, year)
    
if __name__ == '__main__':
    main()

    
