

# LINE 聊天機器人的基本資料


from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import configparser

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = LineBotApi('klg1Ahpgjtq8Umw6vKTk/DKwywjHCNTBRyelpYqcFvfzs6E25OhGBTuajy+pWY8X4oY1xJbMDdKaE3f7vS9+8RdCpO5BlRZvDbbQvtXksOucY30zndTZgW02YQwcD8dWF6IDwKhIh5KWRB5qxNKICwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('8a1480fb9c27152b1f7a9016a09de842')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )

if __name__ == "__main__":
    app.run()