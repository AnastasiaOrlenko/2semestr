from flask import Flask, render_template, request, redirect, url_for
from json import dump, load
app = Flask(__name__)
results = []

@app.route('/')
def index():
    with open('index.json', 'r') as file:
        new = json.load(file)
    new.append(request.args)
    file2 = open('index.json', 'w')
    json.dump(new, file2)
    file2.close()
    return render_template('hhhh.html')
    return new

#@app.route('/stats')
#def stats():
#    return render_template('stats.html')
#    with open('test.json', 'r') as a:
#        return a.read()

#@app.route('/json')
#def jj():
#    return render_template('jj.html')

if __name__ == '__main__':
    app.run(debug=True)
