import re
import os

def table():
    os.system('C:/Users/asus/Desktop/mystem.exe -nd ' + 'C:/Users/asus/Desktop/text.txt' + ' ' + 'C:/Users/asus/Desktop/lemmochki.txt')
    text = open('C:/Users/asus/Desktop/lemmochki.txt', 'r', encoding = 'UTF-8')
    words = text.readlines()
    table = open('C:/Users/asus/Desktop/totable.sql', 'w', encoding = 'utf-8')
    #first = open('C:/Users/asus/Desktop/first.sql', 'w', encoding = 'utf-8')
    table.write('CREATE TABLE lemmas (id INTEGER PRIMARY KEY, word VARCHAR(100), lemma VARCHAR(100);\n')
    #first.write('CREATE TABLE wordforms (id INTEGER PRIMARY KEY, wordform VARCHAR(100);\n')
    idishka = 0
    textposition = 1
    for kek in words:
        regex = re.search('(.*?){(.*?)}', kek)
        wordform = regex.group(1).lower()
        lemma = regex.group(2).lower()
        table.write('INSERT INTO lemmas (id, word, textposition, lemma) VALUES (' + str(idishka) + ', ' + wordform + ', ' + str(textposition) + ', ' + lemma +'); \n')
        #first.write('INSERT INTO lemmas (id, wordform) VALUES (' + str(i) + ', ' + wordform +'); \n')
        idishka += 1
        textposition += 1
    text.close()
    table.close()
    #first.close()

def main():
    table()

if __name__ == '__main__':
    main()

       
 



