"""
controller 負責調用不同的 service 來處理用戶的需求
用戶註冊
用戶資料修改
用戶註銷
一般用戶查詢該用戶信息
上帝用戶查詢多個用戶信息
"""

from services.user_service import UserService
from models.user import User
from flask import Request , Response , jsonify

class UserController:

    @classmethod
    def register(cls, data: Request) -> dict:
        user = User.from_dict(data.json)
        UserService.create_user(user)
        return Response(response="success to create user",status=200,content_type="application/json;charset=utf-8")

    @classmethod
    def get_user(cls, data: Request) -> dict:
        user_id = data.args.get("user_id")
        user = UserService.get_user(user_id)
        if user:
            return user.to_dict()
        else:
            return Response(response="user not found", status=404, content_type="application/json;charset=utf-8")

    @classmethod
    def unregister(cls, data: Request) -> dict:
        user_dict = UserService.delete_user(User.from_dict(data.json))
        return user_dict
