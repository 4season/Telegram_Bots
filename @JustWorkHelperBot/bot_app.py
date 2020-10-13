# A very simple Flask Hello World app for you to get started with...

from flask import Flask,request
import json
import urllib.parse as parse
import urllib.request as req

app = Flask(__name__)


def baseRequest(command="getMe"):
    baseURL = 'https://api.telegram.org/bot1300255931:AAF21AHhfaVaai74cSU-X9giO9pJg27x_gU/'
    res = req.urlopen(baseURL+command) #getMe 로드변수
    result = json.loads(res.read())['result']
    return result

def sendMessage(chat_id, text):
    query = parse.urlencode([
        ('chat_id',chat_id),
        ('text',text)
    ])
    print(query)
    baseRequest('sendMessage?'+query)



@app.route('/')
def hello_world():
    return """
    Hello from Flask! 이 웹사이트는 텔레그램봇 'Just do it!' 을 위해 만들어진 웹사이트 입니다.
    """

@app.route('/1300255931:AAF21AHhfaVaai74cSU-X9giO9pJg27x_gU', methods=['POST','GET'])
def telegram():
    data = request.get_json()
    print(data)
    chat_id = data['message']['chat']['id']
    text = data['message']['text']
    sendMessage(chat_id,text)
    return json.dumps({'success0':True})
