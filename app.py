from flask import Flask , request , abort
from flask_cors import CORS

import os

app = Flask(__name__)
CORS(app)

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from controllers.line_bot_controller import LineBotController
from controllers.user_controller import UserController

line_bot_api = LineBotApi(channel_access_token=os.environ["LINE_CHANNEL_ACCESS_TOKEN"])
handler = WebhookHandler(channel_secret=os.environ["LINE_CHANNEL_SECRET"])

# 載入Follow事件
from linebot.models.events import (
    FollowEvent,UnfollowEvent,MessageEvent,TextMessage,PostbackEvent,ImageMessage,AudioMessage,VideoMessage
)


@app.route("/test")
def test():
    return 'Hello World'

'''
轉發功能列表
'''
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    print(body)
    app.logger.debug('request body is: %s', body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(FollowEvent)
def handle_line_follow(event):
    return LineBotController.follow_event(event)


@app.route("/user")
def get_user():
    return UserController.get_user(request)

if __name__ == '__main__':
    app.run(host="0.0.0.0")