

class UserInfo:
    USERS_NUMBER = 0

    def __init__(self):
        self.user_id = UserInfo.USERS_NUMBER
        UserInfo.USERS_NUMBER += 1
