"""
定義 user 實體 template
"""

from __future__ import annotations

class User(object):
    
    """
    提供 to_dict 和 from_dict 方法，便於 dict 與物件的轉換
    """
    def __init__(self, user_id, user_pic_url, user_nickname, user_system_language, blocked=False) -> None:
        self.user_id = user_id
        self.user_pic_url = user_pic_url
        self.user_nickname = user_nickname
        self.user_system_language = user_system_language
        self.blocked = blocked

    @staticmethod
    def from_dict(source: dict):
        user = User(
            user_id=source.get(u"user_id"),
            user_pic_url=source.get(u"user_pic_url"),
            user_nickname=source.get(u"user_nickname"),
            user_system_language=source.get(u"user_system_language"),
            blocked=source.get(u"blocked")
        )
        # 傳回 user 物件
        return user
        
    
    def to_dict(self) -> dict:
        user_dict = {
            "user_id": self.user_id,
            "user_pic_url": self.user_pic_url,
            "user_nickname": self.user_nickname,
            "user_system_language": self.user_system_language,
            "blocked": self.blocked
        }
        # 傳回 dict
        return user_dict

    def __repr__(self) -> str:
        return (
            f'''User(
            user_id = { self.user_id },
            user_pic_url = { self.user_pic_url },
            user_nickname = { self.user_nickname },
            user_system_language = { self.user_system_language },
            blocked = { self.blocked }
            )'''    )