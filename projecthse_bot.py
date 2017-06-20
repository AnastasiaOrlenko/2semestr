import telebot  # импортируем модуль pyTelegramBotAPI
#import conf     # импортируем наш секретный токен
import urllib.parse
import re
import html
import flask
import os

#WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
#WEBHOOK_URL_PATH = "/{}/".format(conf.TOKEN)
TOKEN = os.environ["425797545:AAEsdrmSrF2nB4FUj_eO7VKr337xIJaEWwM"]
bot = telebot.TeleBot(conf.TOKEN, threaded=False)  # бесплатный аккаунт pythonanywhere запрещает работу с несколькими тредами

# удаляем предыдущие вебхуки, если они были
bot.remove_webhook()

# ставим новый вебхук = Слышь, если кто мне напишет, стукни сюда — url
bot.set_webhook(url="https://serene-waters-34845.herokuapp.com/projecthse_bot")

app = flask.Flask(__name__)

def download_page (link):
    request = urllib.request.Request(link)
    response = urllib.request.urlopen(request)
    result = response.read().decode('cp1251') #кодировка страницы
    #регулярное выражение ищет часть с найденными подсчетами по поиску
    how_many = re.findall ('<p class="found">Найдено <span class="stat-number">(.*?)</span>.*?<span class="stat-caption">(.*?)</span>.*?<span class="stat-number">(.*?)</span>.*?<span class="stat-caption">(.*?)</span>',result)
    #на странице примеры оформлены списком <li>
    texts = re.findall('<li>(.*?)</li>',result)
    return how_many[0], texts[:10] # первые несколько примеров

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Это бот устного корпуса НКРЯ.\n/lex слово - ищет СЛОВО в корпусе')
#вместо этого предложения выше нужно вставить инструкцию какую-то

@bot.message_handler(commands=['lex']) #команда lex поиск слова в корпусе
def send_len(message):
    lex = message.text.replace('/lex','') #берем только слово без команды
    lex = lex.encode ('cp1251') #меняем кодировку
    lex = urllib.parse.quote (lex,safe='') #переводим в процентную кодировку для запроса
    link = 'http://search2.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&dpp=100&spp=50&spd=10&text=lexgramm&mode=spoken&sort=gr_tagging&lang=ru&parent1=0&level1=0&lex1='+\
           lex+\
           '&gramm1=&sem1=&flags1='
    how_many, texts = download_page(link) #функция скачивает страницу выдачи и ищет сколько вхождений и первые примеры
    search = 'Результат:\n'+how_many[0]+' '+how_many[1]+' '+how_many[2]+' '+how_many[3]
    #выводим параметры с поиска - сколько найдено
    bot.send_message(message.chat.id, search)
    #выводим по очереди приеры из выдачи
    for item in texts:
        item = re.sub('<.*?>','',item) #убираем все тэги из html кода, остается текст
        item=html.unescape(item)
        bot.send_message(message.chat.id, item)

#if __name__ == '__main__':
#    bot.polling(none_stop=True)

# пустая главная страничка для проверки
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'ok'


# обрабатываем вызовы вебхука = функция, которая запускается, когда к нам постучался телеграм
@app.route("/projecthse_bot", methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)
        
if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)  
