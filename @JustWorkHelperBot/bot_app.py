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
    print(result)
    return result


def sendMessage(chat_id, text):
    query0 = parse.urlencode([('chat_id', chat_id)])
    query1 = parse.urlencode([('text', text)])
    print(query0)
    print(query1)
    baseRequest('sendMessage?'+query0+'&'+query1)


@app.route('/')
def hello_world():
    return """
    Hello from Flask!
    이 웹사이트는 텔레그램봇 'Just do it!' 을 위해 만들어진 웹사이트 입니다.
    """


@app.route('/1300255931:AAF21AHhfaVaai74cSU-X9giO9pJg27x_gU', methods=['POST','GET'])
def telegram():
    data = request.get_json()
    print(data)
    chat_id = data['message']['chat']['id']
    textM = data['message']['text']
    if textM == '/get_bot_inof':
        text = """
        Just Do It! v(0.1.0)
        귀찮은 작업을 미루지않게 도와주는 봇입니다.
        """
    if textM == '/set_work_new':
        text = """
        할일의 이름을 말씀해주세요.
        """
    if textM == '/get_work_list':
        text = """
        할일이 없다니, 나태하군요.
        """
    if textM == '/set_work_on':
        text = """
        알림을 시작합니다.
        """
    if textM == '/set_work_off':
        text = """
        알림을 종료합니다.
        """
    sendMessage(chat_id,text)
    return json.dumps({'success':True})
