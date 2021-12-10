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
        """
        判斷檔案是否為空，為空直接新增 user，不為空則判斷 user 是否存在
        存在則更新，不存在則新增
        """
        with open("users.json","r",encoding="utf8") as file:
            user_list = json.loads(file.read())
        
        user_dict = user.to_dict()
        with open("users.json","w",encoding="utf-8") as fwrite:
            for i in user_list:
                if i["user_id"] == user_dict["user_id"]:
                    i.update(user_dict)
                    fwrite.write(json.dumps(user_list, indent=2))
                    return user_dict
            user_list.append(user_dict)
            fwrite.write(json.dumps(user_list, indent=2))
            return user_dict
    
    # 刪除 user -> 進行假刪除，將 user 的 blocked 更新為 true 代表刪除的 user
    @classmethod
    def delete(cls, user_id: str):
        """
        用戶存在 -> 進行修改並更新進 users.json
        用戶不存在 -> pass
        """
        with open("users.json","r",encoding="utf8") as file:
            users_list = json.loads(file.read())
            for user_dict in users_list:
                if user_dict["user_id"] == user_id:
                    user_dict["blocked"] = True
                    break
        with open("users.json","w",encoding="utf8") as fwrite:
            fwrite.write(json.dumps(users_list, indent=2))

    def get(user_id: str) -> User:
        with open("users.json","r", encoding="utf8") as file:
            users_list = json.loads(file.read())
            for user_dict in users_list:
                if user_dict["user_id"] == user_id:
                    user = User.from_dict(user_dict)
                    return user
                else:
                    pass