class UserAlreadyExists(Exception):
    def __init__(self, msg='User already exists'):
        super(UserAlreadyExists, self).__init__(msg)


class UserDoesNotExist(Exception):
    def __init__(self, msg='User does not exist'):
        super(UserDoesNotExist, self).__init__(msg)
