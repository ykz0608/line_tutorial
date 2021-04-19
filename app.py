from os import X_OK
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from urllib.parse import parse_qsl

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('sOFovsX2G+IF/aWIeps6rHlREUKXOmt5LsplO/okjzexlavY41Ohq9AwdNTMyiJ2Gm47V+sIZActBR2lhhcl/bP8CzHktTI/7/8efzfzfdPcQCn7brWIl/2YWGKYZG9wRwJ0EsVA4V/ejVNwIXnqmwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('3ea3c4dafa84003e10551844a2f4d830')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

def test1(event):
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://example.com/image.jpg',
        title='你有XXX嗎？',
        text='XXX是。。。。。。。',
        actions=[
            PostbackTemplateAction(
                label='有',
                text='有',
                data='action=step1&itemid=1'
            ),
            PostbackTemplateAction(
                label='沒有',
                text='沒有',
                data='action=step1&itemid=0'
            )
        ]
    )
)
    line_bot_api.reply_message(event.reply_token, message)

def test2(event):
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://example.com/image.jpg',
        title='你有YYY嗎？',
        text='YYY是。。。。。。。',
        actions=[
            PostbackTemplateAction(
                label='有',
                text='有',
                data='action=step2&itemid=1'
            ),
            PostbackTemplateAction(
                label='沒有',
                text='沒有',
                data='action=step2&itemid=0'
            )
        ]
    )
)
    line_bot_api.reply_message(event.reply_token, message)

def test3(event,x):
    y = 2*x[0]+3*x[1]
    if y >= 5:
        message = TextSendMessage('A.由於您的分數未達到%所以。。。')
        line_bot_api.reply_message(event.reply_token, message)
    elif y <= 4:
        message = TextSendMessage('B.由於您的分數未達到%所以。。。')
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage('error。。。')
        line_bot_api.reply_message(event.reply_token, message)

def test4(event,x):
    y = cal(x)
    z = str(y)
    profile_name = line_bot_api.get_profile(event.source.user_id).display_name
    appointment_service_text = '恭喜您已完成我們的測試 {name}的分數為 {z} '.format(name=profile_name,num = z)
    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=[
            TextSendMessage(
                text=appointment_service_text   
            )
        ]
    )

def test5(event,x):
    formula = 4*x[0]+3*x[1]
    if formula >= 5:
        message = TextSendMessage(text='A.由於您的分數達到了30所以是屬於。。。')
        line_bot_api.reply_message(event.reply_token, message)
    elif formula <=4:
        message = TextSendMessage(text='B.由於您的分數未達到30所以是屬於。。。')
        line_bot_api.reply_message(event.reply_token, message)

def test6(event):
    formula = 20*x[0]+3*x[1]
    result_text = '由於您的分數是{no}這個區間，達到了5分屬於'.format(no=formula)
    if formula >= 5:
        message = TextSendMessage(result_text+'a')
        line_bot_api.reply_message(event.reply_token, message)
    elif formula <=4:
        message = TextSendMessage(result_text+'b')
        line_bot_api.reply_message(event.reply_token, message)

def test7(event):
    formula = 3*x[0]+4*x[1]
    result_text = '由於您的分數是{no}這個區間，達到了5分屬於'.format(no=formula)
    if formula >= 5:
        message = TextSendMessage(result_text+'a')
        line_bot_api.reply_message(event.reply_token, message)
    elif formula <=4:
        message = TextSendMessage(result_text+'b')
        line_bot_api.reply_message(event.reply_token, message)

    message = TextSendMessage('x')
    line_bot_api.reply_message(event.reply_token, message)


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)
    message_text = str(event.message.text).lower()

    if message_text =='ai':
        test1(event)
    elif message_text =='有':
        pass
    elif message_text == '沒有':
        pass
    else:
        message = TextSendMessage(text='請輸入關鍵字“ai”開始我們的測試')
        line_bot_api.reply_message(event.reply_token, message)


@handler.add(PostbackEvent)
def handler_postback(event):
    # 我們需要把拿到的data字串轉換成字典，那我們會使用urllib裡的prase_qsl
    # prase_qsl可以解析一個query字串把它轉換成一個list
    # 那list如果要轉換成字典，在前面加上dict即可
    # 有了字典就可以針對action和server去取得資料（action和server是自定義宣告的，可以做更換）

    data = dict(parse_qsl(event.postback.data))
    action_data = data.get('action')
    num_data = data.get('itemid')
    x=[]
    # 接著就是做判斷，判斷我們的action等於什麼，然後做什麼事
    # 那我們這邊判斷如果等於step2，我們就做預約的動作

    if action_data == 'step1':
        if num_data =='1':
            x.append(1.0)
        elif num_data =='0':
            x.append(0.0)
        test2(event) 
    elif action_data == 'step2':
        if num_data =='1':
            x.append(1.0)
        elif num_data=='0':
            x.append(0.0)
        test7(event)
    return x
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
