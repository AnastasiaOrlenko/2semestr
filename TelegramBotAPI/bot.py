import flask
import telebot
import conf

WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(conf.TOKEN)

bot = telebot.TeleBot(conf.TOKEN, threaded=False)
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)

app = flask.Flask(__name__)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Приветики, давай я посчитаю тебе слова в тексте:)")


@bot.message_handler(func=lambda m: True)
def send_len(message):
    text_without_simbols = []
    text_with_simbols = message.text.split()
    for element in text_with_simbols:
        element = element.strip(' .,;:?!&1234567890{}()[]«»-_=+"<>#\*^@`/')
        if element != '':
            text_without_simbols.append(element)
        count = str(len(text_without_simbols))
    bot.send_message(message.chat.id, 'Хммм, ну смотри, у тебя тут их {}.'.format(count))


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'ok'


@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)
