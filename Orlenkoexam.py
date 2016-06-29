import re 

def opening():
    f = open('spb.txt', 'r', encoding = 'UTF-8')
    file = f.read()
    res = re.findall('[А-Я]\.\s?[А-Я][а-я]+',file)
    for t in res:
        print(t)
    f.close()
    return file

def names(file):
    f1 = open('spb.txt', 'r', encoding = 'UTF-8')
    file1 = f1.read()
    res1 = re.findall('[А-Я][а-я]+\s[А-ЯЁ][а-яё]+',file1)
    res2 = re.findall('[А-Я]\.\s?[А-Я]?\.?\s?[А-ЯЁ][а-яё]+',file1)
    kek = res1 + res2
    for t1 in kek:
        print(t1)
    
def main():
    file = opening()
    names(file)
    
if __name__ == '__main__':
    main()
