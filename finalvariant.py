import urllib.request 
import os
import re

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        return page.read().decode('utf-8')
    except:
        print('Error at', pageUrl)
        return None

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

def metadata(path, author, header, date, topic, link, year):
    row = '%s\t%s\t\t\t%s\t%s\tпублицистика\t\t\t%s\t\tнейтральный\tн-возраст\tн-уровень\tгородская\t%s\tБАМ\t\t%s\tгазета\tРоссия\tРеспубликаБашкортостан\tru'
    path = path + os.sep + '.txt'
    filee = open('С:' + os.sep + 'MestnoeVremya' + os.sep + 'metadata.csv', 'w', encoding = 'utf-8')
    filee.write(row % ('path', 'author', 'header', 'date', 'topic', 'link', 'year'))
    filee.close()

def func1(article, path, header, author, date, topic, link):
    row = '@au %s\n@ti %s\n@da %s\n@topic %s\n@url %s\n%s'
    if not os.path.exists(path):
        os.makedirs(path)
    fw = open(path + os.sep + '.txt', 'w', encoding = 'utf-8')
    fw.write(row %(author, header, date, topic, link, article))
    fw.close()
        
def func2():
    for root, dirs, files in os.walk('C:' + os.sep + 'MestnoeVremya' + os.sep + 'plain'):
        for fl in files:
            put = root.replace('plain', 'mystem-xml')
            if not os.path.exists(put):
                os.makedirs(put)
            x = root + os.sep + fl
            y = x.replace('plain', 'mystem-xml')
            y = y.replace('.txt', '.xml') 
            os.system(r'C:\mystem.exe -ncid --format xml ' + x + ' ' + y)

def func3():
    for root, dirs, files in os.walk('C:' + os.sep + 'MestnoeVremya' + os.sep + 'plain'):
        for i in files:
            put = root.replace('plain', 'mystem-plain')
            if not os.path.exists(rout):
                os.makedirs(rout)
            x = root + os.sep + i
            y = x.replace('plain', 'mystem-plain')        
            os.system(r'C:\mystem.exe -ncid ' + x + ' ' + y)
                

def main():
    commonUrl = 'http://gazeta-bam.ru/article/'
    article = []
    for i in range(1227, 115223):
        pageUrl = commonUrl + str(i)
        article.append(download_page(pageUrl))
    download_page(pageUrl)
    html = stranica(pageUrl)
    html = article(html)
    date, month, year = get_date(html)
    header = get_header(html)
    topic = get_topic(html)
    metadata(path, author, header, date, topic, link, year)
    func1(article, path, header, author, date, topic, link)
    func2()
    func3()
    
if __name__ == '__main__':
    main()
