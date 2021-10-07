from config import URL


class MoodleWrongCredentials(Exception):
    def __init__(self, msg=f'There is no such user at {URL}'):
        super(MoodleWrongCredentials, self).__init__(msg)
