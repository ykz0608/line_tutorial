from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)

    message = TemplateSendMessage(
        alt_text='AI',
        template=ConfirmTemplate(
            text='你有XXX嗎?',
            actions=[
                PostbackTemplateAction(
                    label='有',
                    text='postback text',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='沒有',
                    text='message text'
                    data='action=buy&itemid=-0'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
