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

def AS1(event):
    message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='您曾經患有脊椎發炎嗎?',
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

def Age0(event):
    message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='請選擇您的年齡區間',
        actions=[
            PostbackTemplateAction(
                label='60嵗以上',
                text='有',
                data='action=step20'
            ),
            PostbackTemplateAction(
                label='60嵗以下',
                text='沒有',
                data='action=step21'
            )
        ]
    )
)
    line_bot_api.reply_message(event.reply_token, message)

def Age1(event):
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        title='請選擇您的年齡區間',
        text='XXX是。。。。。。。',
        actions=[
            PostbackTemplateAction(
                label='20-29',
                text='1',
                data='action=step22&itemid=24.5'
            ),
            PostbackTemplateAction(
                label='30-39',
                text='1',
                data='action=step22&itemid=34.5'
            ),
            PostbackTemplateAction(
                label='40-49',
                text='1',
                data='action=step22&itemid=44.5'
            ),
            PostbackTemplateAction(
                label='50-59',
                text='1',
                data='action=step22&itemid=54.5'
            )
        ]
    )
)
    line_bot_api.reply_message(event.reply_token, message)

def Age2(event):
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        title='請選擇您的年齡區間',
        text='XXX是。。。。。。。',
        actions=[
            PostbackTemplateAction(
                label='60-69',
                text='1',
                data='action=step22&itemid=64.5'
            ),
            PostbackTemplateAction(
                label='70-79',
                text='1',
                data='action=step22&itemid=74.5'
            ),
            PostbackTemplateAction(
                label='80-89',
                text='1',
                data='action=step22&itemid=84.5'
            ),
            PostbackTemplateAction(
                label='90-99',
                text='1',
                data='action=step22&itemid=94.5'
            )
        ]
    )
)
    line_bot_api.reply_message(event.reply_token, message)

def sex(event):
    message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='您的性別是?',
        actions=[
            PostbackTemplateAction(
                label='男性',
                text='男性',
                data='action=step3&itemid=1'
            ),
            PostbackTemplateAction(
                label='女性',
                text='女性',
                data='action=step3&itemid=0'
            )
        ]
    )
)
    line_bot_api.reply_message(event.reply_token, message)

def DM(event):
    message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='您曾經患有糖尿病嗎?',
        actions=[
            PostbackTemplateAction(
                label='有',
                text='有',
                data='action=step4&itemid=1'
            ),
            PostbackTemplateAction(
                label='沒有',
                text='沒有',
                data='action=step4&itemid=0'
            )
        ]
    )
)
    line_bot_api.reply_message(event.reply_token, message)

def hyper(event):
    message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='您曾經患有高血壓嗎?',
        actions=[
            PostbackTemplateAction(
                label='有',
                text='有',
                data='action=step5&itemid=1'
            ),
            PostbackTemplateAction(
                label='沒有',
                text='沒有',
                data='action=step5&itemid=0'
            )
        ]
    )
)
    line_bot_api.reply_message(event.reply_token, message)

def hyplip(event):
    message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='您曾經患有高血酯嗎?',
        actions=[
            PostbackTemplateAction(
                label='有',
                text='有',
                data='action=step6&itemid=1'
            ),
            PostbackTemplateAction(
                label='沒有',
                text='沒有',
                data='action=step6&itemid=0'
            )
        ]
    )
)
    line_bot_api.reply_message(event.reply_token, message)

def CHD(event):
    message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='您曾經患有心臟病嗎?',
        actions=[
            PostbackTemplateAction(
                label='有',
                text='有',
                data='action=step7&itemid=1'
            ),
            PostbackTemplateAction(
                label='沒有',
                text='沒有',
                data='action=step7&itemid=0'
            )
        ]
    )
)
    line_bot_api.reply_message(event.reply_token, message)

def COPD(event):
    message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='您曾經患有呼吸阻塞症嗎?',
        actions=[
            PostbackTemplateAction(
                label='有',
                text='有',
                data='action=step8&itemid=1'
            ),
            PostbackTemplateAction(
                label='沒有',
                text='沒有',
                data='action=step8&itemid=0'
            )
        ]
    )
)
    line_bot_api.reply_message(event.reply_token, message)

def CHv(event):
    message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='您曾經患有慢性支氣管炎嗎?',
        actions=[
            PostbackTemplateAction(
                label='有',
                text='有',
                data='action=step9&itemid=1'
            ),
            PostbackTemplateAction(
                label='沒有',
                text='沒有',
                data='action=step9&itemid=0'
            )
        ]
    )
)
    line_bot_api.reply_message(event.reply_token, message)

def Stroke(event):
    message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='您曾經患有中風嗎?',
        actions=[
            PostbackTemplateAction(
                label='有',
                text='有',
                data='action=step10&itemid=1'
            ),
            PostbackTemplateAction(
                label='沒有',
                text='沒有',
                data='action=step10&itemid=0'
            )
        ]
    )
)
    line_bot_api.reply_message(event.reply_token, message)

def question1(event):
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

def question2(event):
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

def test5(event):
    formula = 4*x[0]+3*x[1]
    if formula >= 5:
        message = TextSendMessage(text='A.由於您的分數達到了30所以是屬於。。。')
        line_bot_api.reply_message(event.reply_token, message)
    elif formula <=4:
        message = TextSendMessage(text='B.由於您的分數未達到30所以是屬於。。。')
        line_bot_api.reply_message(event.reply_token, message)

def result(event):
    formula = -2.1+0.39*x[0]+0.038*x[1]-0.554*x[2]+0.848*x[3]+0.147*x[4]+0.623*x[5]-0.06*x[6]+0.267*x[7]+0.178*x[8]+0.459*x[9]
    result_text = '五十肩由於您的分數是{no}這個區間，屬於'.format(no=formula)
    if formula >= 6:
        message = TextSendMessage(result_text+'a')
        line_bot_api.reply_message(event.reply_token, message)
    elif formula <=5:
        message = TextSendMessage(result_text+'b')
        line_bot_api.reply_message(event.reply_token, message)


# def test7(event):
#     formula = 3*x[0]+4*x[1]
#     result_text = '由於您的分數是{no}這個區間，達到了5分屬於'.format(no=formula)
#     if formula >= 5:
#         message = TextSendMessage(result_text+'a')
#         line_bot_api.reply_message(event.reply_token, message)
#     elif formula <=4:
#         message = TextSendMessage(result_text+'b')
#         line_bot_api.reply_message(event.reply_token, message)



# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)
    message_text = str(event.message.text).lower()
    pass_keyword = ['男性','女性','有','沒有','1']

    if message_text =='ai':
        AS1(event)
    elif message_text in pass_keyword:
        pass
    else:
        message = TextSendMessage(text='您好，請輸入關鍵字“ai”開始我們的測試')
        line_bot_api.reply_message(event.reply_token, message)

x = []

@handler.add(PostbackEvent)
def handler_postback(event):
    # 我們需要把拿到的data字串轉換成字典，那我們會使用urllib裡的prase_qsl
    # prase_qsl可以解析一個query字串把它轉換成一個list
    # 那list如果要轉換成字典，在前面加上dict即可
    # 有了字典就可以針對action和server去取得資料（action和server是自定義宣告的，可以做更換）

    data = dict(parse_qsl(event.postback.data))
    action_data = data.get('action')
    num_data = data.get('itemid')
    # 接著就是做判斷，判斷我們的action等於什麼，然後做什麼事
    # 那我們這邊判斷如果等於step2，我們就做預約的動作

    if action_data == 'step1':
        del x[:]
        if num_data =='1':
            x.append(1)
        elif num_data =='0':
            x.append(0)
        Age0(event) 
    elif action_data == 'step20':
        Age1(event)
    elif action_data == 'step21':
        Age2(event)
    elif action_data =='step22':
        if num_data=='24.5':
            x.append(24.5)
        elif num_data=='34.5':
            x.append(34.5)
        elif num_data=='44.5':
            x.append(44.5)
        elif num_data=='54.5':
            x.append(54.5)
        elif num_data=='64.5':
            x.append(64.5)
        elif num_data=='74.5':
            x.append(74.5)
        elif num_data=='84.5':
            x.append(84.5)
        elif num_data=='94.5':
            x.append(94.5)
        sex(event)
    elif action_data == 'step3':
        if num_data =='1':
            x.append(1)
        elif num_data=='0':
            x.append(0)
        DM(event)
    elif action_data == 'step4':
        if num_data =='1':
            x.append(1)
        elif num_data=='0':
            x.append(0)
        hyper(event)
    elif action_data == 'step5':
        if num_data =='1':
            x.append(1)
        elif num_data=='0':
            x.append(0)
        hyplip(event)
    elif action_data == 'step6':
        if num_data =='1':
            x.append(1)
        elif num_data=='0':
            x.append(0)
        CHD(event)
    elif action_data == 'step7':
        if num_data =='1':
            x.append(1)
        elif num_data=='0':
            x.append(0)
        COPD(event)
    elif action_data == 'step8':
        if num_data =='1':
            x.append(1)
        elif num_data=='0':
            x.append(0)
        CHv(event)
    elif action_data == 'step9':
        if num_data =='1':
            x.append(1)
        elif num_data=='0':
            x.append(0)
        Stroke(event)
    elif action_data == 'step10':
        if num_data =='1':
            x.append(1)
        elif num_data=='0':
            x.append(0)
        result(event)
    
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
