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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text='您有XXX嗎？？',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=PostbackAction(
                            label='有',
                            text='1.有',
                            data='action=step2'
                        )
                    ),
                    QuickReplyButton(
                        action=PostbackAction(
                            label='沒有',
                            text='1.沒有',
                            data='action=step2'
                        )
                    )
                ]
            )
        )
    )

def test2(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text='您有YYY嗎？？',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=PostbackAction(
                            label='有',
                            text='2.有',
                            data='action=step3'
                        )
                    ),
                    QuickReplyButton(
                        action=PostbackAction(
                            label='沒有',
                            text='2.沒有',
                            data='action=step3'
                        )
                    )
                ]
            )
        )
    )
x=0

def test3(event):

    message = TextSendMessage(x)
    line_bot_api.reply_message(event.reply_token, message)

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)
    message_text = str(event.message.text).lower()

    if message_text =='ai':
        test1(event)
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
    text_data = data.get('text')

    # 接著就是做判斷，判斷我們的action等於什麼，然後做什麼事
    # 那我們這邊判斷如果等於step2，我們就做預約的動作
    if action_data == 'step2':
        test2(event)
    elif action_data == 'step3':
        test3(event)

    if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
