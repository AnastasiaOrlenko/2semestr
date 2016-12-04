import re
import html
import urllib.request


def func1(website): 
    req = urllib.request.Request(website)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    return html
        
        
A = []
def poisk():
    sites = ['http://runews24.ru/culture/03/12/2016/0b1e9ad3de5d3a866840728cb5fe9110','http://www.vesti.ru/doc.html?id=2828727','https://www.ridus.ru/news/238039', 'http://gosindex.ru/news/kultura/ivan-ohlobystin']
    for i in sites:
        wep = func1(i)
        regex = re.search ('<div (class="desc text"|class="js-mediator-article"|class="post_message")>(.*?)</div>', wep, flags = re.DOTALL)
        new_text = re.findall(regex.group(2), wep)
        new_element = new_text
        A.append(new_element)
        
    return new_text


        
def process(new_text):
    regul = re.compile('<div.*?>.*?</div>', flags=re.DOTALL)
    regTag = re.compile('<.*?>', flags=re.DOTALL) 
    regScript = re.compile('<script.*?>.*?</script>', flags=re.DOTALL) 
    regComment = re.compile('<!--.*?-->', flags=re.DOTALL) 
    regSpace = re.compile('\s{2,}', flags = re.DOTALL)
    good_text= [] 
    for t in new_text:
        lite = regSpace.sub(" ", t)
        lite = regul.sub(" ", lite)
        lite = regScript.sub(" ", lite)
        lite = regTag.sub(" ", lite)
        lite = regComment.sub(" ", lite)
        lite = html.unescape(lite)
        good_text.append(lite)            
        for t in good_text:
            a = t.split(' ')
            listik = []
            for elem in a:
                elem = elem.strip(',./\?":;!@#$%^&*()-_=+»«"1—234567890\n\t\xa0')
                elem = elem.lower()
                if elem !='':
                    listik.append(elem)
            q = set(listik)                
        return q

def per():
    new_text = poisk()
    q = process(new_text)
    z = q.copy()
    for k in A:
        stroka = k
        q =  process(k)
        o = q.copy()
        z = o & z
    p = z.copy()
    x = list(p)
    x.sort()
    q_c = x
    return(q_c)
        
def obj():
    new_text = poisk()
    q = process(new_text)
    z = q.copy()
    for k in A:
        stroka = k
        q =  process(k)
        o = q.copy()
        z = o | z
    p = z.copy()
    x = list(p)
    x.sort()
    q_d = x
    return(q_d)

def sim_raz():
    b = set(obj()) ^ set(per())
    c = list(b)
    c.sort()
    return (c)
            
def write_difference(c):
    fw = open('simraz.txt.', 'w', encoding = 'utf-8')
    for new in c:
        fw.write(new + '\n')
    fw.close()
    
def write_common(q_c):
    fw = open('obshee.txt.', 'w', encoding = 'utf-8')
    for element in q_c:
        fw.write(element + '\n')
    fw.close()

def main ():
    
    new_text = poisk()
    q = process(new_text)
    q_c = per()
    q_d = obj()
    c = sim_raz()
    write_difference(c)
    write_common(q_c)
   
        
if __name__ == '__main__':
    main()
