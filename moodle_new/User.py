import re
import requests
from bs4 import BeautifulSoup
from requests import Session, post

from exceptions.moodle_exceptions import MoodleWrongCredentials
from config import URL, ENDPOINT, LOGIN_URL
from moodle_new.moodle_api import *


class User:
    """Class for a single user.

    Example:
    >>> User(username='john.dou@nure.ua')
    """

    def __init__(self, login, pswd, **data):
        self.login = login
        self.pswd = pswd
        self.token = self.__get_user_token(login, pswd)

    def __get_user_token(self, login, pswd):
        data = {
            'username': login,
            'password': pswd,
            'service': 'moodle_mobile_app'
        }
        s = Session()
        response = s.get('https://dl.nure.ua/login/token.php', params=data)
        if 'error' in response.json():
            raise MoodleWrongCredentials

        response = response.json()
        token = response['token']
        # private_token = response['privatetoken']
        # print(f'User token "{token}" was used.')
        return token

    def call(self, fname, **kwargs):
        """Calls moodle API function with function name fname and keyword arguments.

        Example:
        >>> call('core_course_update_courses', courses = [{'id': 1, 'fullname': 'My favorite course'}])
        """
        parameters = rest_api_parameters(kwargs)
        parameters.update({"wstoken": self.token, 'moodlewsrestformat': 'json', "wsfunction": fname})
        # print(parameters)
        response = post(URL + ENDPOINT, parameters)
        response = response.json()

        if type(response) == dict and response.get('exception'):
            raise SystemError("Error calling Moodle API\n", response)
        return response

    def __login(self, session):
        r = session.get(url=URL + "/login/index.php")
        soup = BeautifulSoup(r.text, 'html.parser')
        token = soup.find('input', attrs={'name': 'logintoken'})['value']
        login_data = {
            'anchor': '',
            'logintoken': token,
            'username': self.login,
            'password': self.pswd,
            'rememberusername': 0
        }
        response = session.post(url=LOGIN_URL, data=login_data)
        if 'error' in response.json():
            raise MoodleWrongCredentials
        return session

    def check_attendance_by(self, course):
        """
        http://localhost/webservice/rest/server.php?&
        wsfunction=mod_wsattendance_get_session&
        sessionid=22&moodlewsrestformat=json&
        wstoken=bd9931ef5caa93f2bfc180646971a014
        """
        # from requests_html import HTMLSession
        # session = HTMLSession()
        session = requests.Session()

        self.login(session)
        course_att_id = course.get_modules()['Відвідування']['id']
        r = session.get("https://dl.nure.ua/mod/attendance/view.php?id=" + str(course_att_id))
        submit = re.compile(r'mod\/attendance\/attendance.php\?sessid=(\d+)&amp;sesskey=(\w+)')
        search = submit.search(r.text)

        if not search:
            print('ERROR there is no attendance button')
            return
        # todo add exception instead

        present_status = 'Присутствовал'
        sessid = search.group(1)
        sesskey = search.group(2)

        data = {
            "status": present_status,
            "sessid": sessid,
            "sesskey": sesskey,
            "_qf__mod_attendance_student_attendance_form": "1",
            "mform_isexpanded_id_session": "1",
            "submitbutton": "Save+changes"
        }

        r = session.post('https://dl.nure.ua/mod/attendance/attendance.php', data=data)
