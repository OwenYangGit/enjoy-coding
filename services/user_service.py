import os

from models.user import User
from daos.user_dao import UserMySQLDao

from typing import List
from linebot import LineBotApi
from linebot.exceptions import LineBotApiError

class UserService:

    line_bot_api = LineBotApi(channel_access_token=os.environ["LINE_CHANNEL_ACCESS_TOKEN"])

    @classmethod
    def user_follow(cls, event):

        print(event)

        user_id = event.source.user_id

        print(user_id)

        try:
            user_profile = cls.line_bot_api.get_profile(user_id)
        except LineBotApiError as e:
            pass

        # TODO: line_user_pic_url 待處理，先暫時存 line 給的 url

        user = User(
            line_user_id=user_profile.user_id,
            line_user_pic_url=user_profile.picture_url,
            line_user_nickname=user_profile.display_name,
            line_user_status=user_profile.status_message,
            line_user_system_language=user_profile.language,
            message_files=None,
            image_files=None,
            audio_files=None,
            video_files=None,
            blocked=False
        )
        print(user)
        UserMySQLDao.add_user(user)

        pass

    @classmethod
    def get_user(cls, user_id: str) -> User:

        user = UserMySQLDao.get_user(user_id)

        return user

    @classmethod
    def get_images(cls, user_id: str) -> List[str]:

        user = UserMySQLDao.get_user(user_id)
        user_images_files = user.image_files

        return user_images_files

    @classmethod
    def get_videos(cls, user_id) -> List[str]:

        user = UserMySQLDao.get_user(user_id)
        user_videos_files = user.video_files

        return user_videos_files