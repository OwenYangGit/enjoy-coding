"""
處理操作 DAO 前後要做的事情
創建用戶
更新用戶
刪除用戶
查找用戶
一次查看特定幾個用戶
一次創建多個用戶
一次刪除多個用戶
"""

from daos.user_dao import UserDAO
from models.user import User

class UserService:
    
    # 創建用戶
    @classmethod
    def create_user(cls, user: User):
        user.blocked=False
        return UserDAO.save(user)

    # 更新用戶
    @classmethod
    def update_user(cls, user: User):
        user_dict = user.to_dict()
        user_info = UserDAO.get(user_dict["user_id"])
        if user_info and user_info["blocked"] != True:
            UserDAO.save(user)
            return user.to_dict()
        else:
            pass
        
    # 刪除用戶
    @classmethod
    def delete_user(cls, user: User) -> dict:
        user_dict = user.to_dict()
        user_id = user_dict["user_id"]
        UserDAO.delete(user_id)
        print(user_dict)
        user = UserDAO.get(user_id)
        return user.to_dict()

    @classmethod
    def get_user(cls, user_id: str) -> User:
        user = UserDAO.get(user_id)
        return user