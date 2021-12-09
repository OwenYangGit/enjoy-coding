"""
controller 負責調用不同的 service 來處理用戶的需求
用戶註冊
用戶資料修改
用戶註銷
一般用戶查詢該用戶信息
上帝用戶查詢多個用戶信息
"""

from services.user_service import UserService
from flask import Request , Response
import json

class UserController:
    