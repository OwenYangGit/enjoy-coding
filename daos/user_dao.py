"""
提供 user 物件針對存取的操作
簡單說就是針對 user 物件的 crud 操作
本範例的存儲載體以 filesystem 為載體
"""

from models.user import User
import json

class UserDAO:
    """
    DAO 物件要有創建，查找，更新，刪除等操作
    """

    # 存 user 物件，若 user 存在，採更新
    @classmethod
    def save(cls, user: User):
        with open("users.json","rw",encoding="utf8") as file:
            users_list = json.loads(file.read())
            # convert user to user_dict
            user_dict = user.to_dict()
            for index, user in enumerate(users_list):
                if user["user_id"] == user_dict["user_id"]:
                    users_list[index] = user.update(user_dict)
                    file.write(json.dumps(users_list))
                else:
                    user_dict = user.to_dict()
                    users_list.append(user_dict)
                    file.write(json.dumps(users_list))
        return user.to_dict()
    
    # 刪除 user -> 進行假刪除，將 user 的 blocked 更新為 true 代表刪除的 user
    @classmethod
    def delete(cls, user_id: str):
        with open("users.json","rw",encoding="utf8") as file:
            users_list = json.loads(file.read())
            for user_dict in users_list:
                if user_dict["user_id"] == user_id:
                    user_dict["blocked"] = True
            file.write(json.dumps(users_list))

    def get(user_id: str) -> User:
        with open("users.json","r", encoding="utf8") as file:
            users_list = json.loads(file.read())
            for user_dict in users_list:
                if user_dict["user_id"] == user_id:
                    user = User.from_dict(user_dict)
                    return user
                else:
                    pass
        