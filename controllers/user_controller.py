from flask import Request
from services.user_service import UserService

class UserController:
    
    @classmethod
    def get_user(cls, request: Request):
        user_id = request.args.get("line_user_id")
        user = UserService.get_user(user_id)
        return user.to_dict()