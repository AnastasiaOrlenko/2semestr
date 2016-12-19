import re
import html
import urllib.request
import os

def opening():
    file = open('C:/Users/student/Desktop/papka/adg.html', 'r', encoding = 'UTF-8')
    code = file.read()
    regex = re.compile('<div class="categories">.*?<h1><a href=\".*?\">(.*?)<div class="posted">',flags=re.U | re.DOTALL)
    new = re.findall(regex, code)
    mass = []
    regTag = re.compile('<.*?>', flags=re.DOTALL)
    regSpace = re.compile('\s{2,}', flags = re.DOTALL)
    for k in new:
        lite = regSpace.sub(" ", k)
        lite = regTag.sub(" ", lite)
        mass.append(lite)
        for k in mass:
            a = k.split(' ')
            listik = []
            for elem in a:
                elem = elem.strip('0123456789»«,./\?":;!@#$%^&*()-_=+"—\n\t\xa0')
                elem = elem.lower()
                if elem !='':
                    listik.append(elem)
            q = set(listik)                
        return q

def adyghe():
    words = set()
    f = open('C:/Users/student/Desktop/papka/adyghe-unparsed-words.txt', 'r', encoding='utf-8')
    for word in f.readlines():
        if word not in words:
            words.add(word.strip('\n'))
    return words
    

def peresechenie():
    file_new = open('C:/Users/student/Desktop/papka/file.txt', 'w', encoding = 'UTF-8')
    words = adyghe()
    q = opening()
    z = q & words
    return z

def file_peres(z):
    spisok = open('C:/Users/student/Desktop/papka/wordlist.txt', 'w', encoding = 'UTF-8')
    for element in z:
        spisok.write(element + '\n')
    spisok.close()

def mystemm():
    os.system("C:/Users/student/Desktop/papka/mystem.exe " + " adyghe-unparsed-words.txt" + "rus_nouns.txt" + ' -cnid')
    keks = open('C:/Users/student/Desktop/papka/rus_nouns.txt', 'r', encoding = 'UTF-8')
    slovechki = keks.readlines()
    keks.close ()
    rus_nouns = []
    reg = 'S[a-z,=]*?(nom,sg)'
    for lem in slovechki:
        text = re.search (reg, lem)
        if text:
            russkoe = text.group(1)
            rus_nouns.append(russkoe)
       
    nouns = ''
    for i in rus_nouns:
        nouns = nouns + i + '\n'       
    keks = open('C:/Users/student/Desktop/papka/rus_nouns.txt', 'w', encoding = 'UTF-8')
    keks.write(nouns)
    keks.close()    
#тут покидала идеи. все пятьсот раз постирала. оставила только такой вариант. но в нем не уверена, поскольку не работает

    
def main():
    q = opening()
    words = adyghe()
    z = peresechenie()
    file_peres(z)
    mystemm()
    
    
if __name__ == '__main__':
    main()
