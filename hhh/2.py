from flask import Flask, render_template, request, redirect, url_for
from json import dumps, loads
import re
app = Flask(__name__)

@app.route('/')
def index():
    if request.args:
        #lol = open('cifr.json', 'r', encoding='utf-8')
        #mem = lol.read()
        #resultat = mem.split('\t')
        #for i in range(len(resultat)):
        #    resultat[i] = int(resultat[i])
        #lol.close()
        #lol = open('cifr.json', 'w', encoding='utf-8')
        #if request.args['answer'] == 'kotik':
        #    resultat[0] += 1
        #if request.args['answer'] == 'koshechka':
        #   resultat[1] += 1
        #if request.args['answer'] == 'kisa':
        #    resultat[2] += 1
        #if request.args['answer'] == 'kosharik':
        #    resultat[3] += 1
        #lol.write(dumps(resultat, ensure_ascii=False))
        #lol.close()
        
        file = open('index.json', 'r', encoding='utf-8')
        new = file.read()
        results = loads(new)
        results[request.args['username']] = request.args['answer']
        file.close()
        file = open('index.json', 'w', encoding='utf-8')
        file.write(dumps(results, ensure_ascii=False))
        file.close()
        return redirect(url_for('statistic'))
    return render_template('hhhh.html')

@app.route('/stats')
def statistic():
    file = open('index.json', 'r', encoding='utf-8')
    kek = file.read()
    slovarik = loads(kek)
    answers = []
    for key in slovarik:
        answer = slovarik[key]
        answers.append(answer)
        file.close()
    return render_template('stat.html', answer=answers)

@app.route('/json')
def jsonn():
    lelik = open('index.json', 'r')
    f = lelik.read()
    lelik.close()
    q = f.split('\n')
    jsonn = dumps(q)
    return jsonn
    return render_template('jsonn.json')

#@app.route('/search')
#def search():
#    if request.args:
#        word = request.args['answer']
#        filik = open ('stat.json', 'r')
#        words = filik.read().split()
#        filik.close()
#        b = []
#        for i in range (len(words)):
#            if word == words[i].strip(':'):
                
if __name__ == '__main__':
    app.run(debug=True)
