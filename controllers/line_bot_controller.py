import os

from services.user_service import UserService

from linebot import (
    LineBotApi
)

'''
處理所有從 LINEBOT 送過來的 Event
'''
class LineBotController:
    line_bot_api = LineBotApi(channel_access_token=os.environ["LINE_CHANNEL_ACCESS_TOKEN"])

    @classmethod
    def follow_event(cls, event):
        UserService.user_follow(event)
        return 'OK'