import datetime
from pprint import pprint
from time import ctime

from config import URL
from moodle_new.Course import Course
from moodle_new.User import User


class Calendar:

    def __init__(self, user: User):
        self.user = user
        self.today_date = datetime.date.today()

    def get_month_view(self, month, year, mini=1):
        month = self.user.call("core_calendar_get_calendar_monthly_view", month=month, year=year, mini=mini)
        month_events = {}
        for week in month['weeks']:
            for day in week['days']:
                for field in day['events']:
                    if field['eventtype'] != 'attendance':
                        continue
                    time = field['timestart']
                    time = datetime.datetime.fromtimestamp(time)
                    course = Course(self.user, **field['course'])
                    month_events.update({time: course})
        return month_events

    def get_current_month_view(self, mini=1):
        month = self.today_date.month
        year = self.today_date.year
        return self.get_month_view(month, year, mini)

    def get_week_view(self, day, month, year, mini=1):
        int_day = int(day)
        week_events = {}
        month = self.user.call("core_calendar_get_calendar_monthly_view", month=month, year=year, mini=mini)
        for week in month['weeks']:
            for day in week['days']:
                int_mday = int(day['mday'])
                if int_mday != int_day:
                    continue
                # starts over from Monday to store all classes for the current week
                for day in week['days']:
                    for field in day['events']:
                        if field['eventtype'] != 'attendance':
                            continue
                        time = field['timestart']
                        time = datetime.datetime.fromtimestamp(time)
                        course = Course(self.user, **field['course'])
                        # print(time, course.get_field('fullname'))
                        week_events.update({time: course})
                break
        return week_events

    def get_current_week_view(self, mini=1):
        day = self.today_date.day
        month = self.today_date.month
        year = self.today_date.year
        return self.get_week_view(day, month, year, mini)

    def get_day_view(self, day, month, year):
        day_events = {}
        day = self.user.call('core_calendar_get_calendar_day_view', day=day, month=month, year=year)
        for field in day['events']:
            if field['eventtype'] != 'attendance':
                continue
            time = field['timestart']
            time = datetime.datetime.fromtimestamp(time)
            course = Course(self.user, **field['course'])
            # print(time, cou,rse.get_field('fullname'))
            day_events.update({time: course})
        return day_events

    def get_current_day_view(self):
        day = self.today_date.day
        month = self.today_date.month
        year = self.today_date.year
        return self.get_day_view(day, month, year)

    def get_upcoming_events(self):
        upcoming_events = {}
        events = self.user.call('core_calendar_get_calendar_upcoming_view')
        for field in events['events']:
            if field['eventtype'] != 'attendance':
                continue
            time = field['timestart']
            time = datetime.datetime.fromtimestamp(time)
            course = Course(self.user, **field['course'])
            # print(time, course.get_field('fullname'))
            upcoming_events.update({time: course})
        return upcoming_events



    def get_cal_export_link(self):
        token = self.user.call('core_calendar_get_calendar_export_token')

        token = token['token']
        userid = 14176

        class preset_what:
            all = 'all'                 # Все события
            categories = 'categories'   # События, связанные с категориями
            courses = 'courses'         # События курса
            groups = 'groups'           # События, связанные с группами
            user = 'user'               # Мои личные события

        class preset_time:
            weeknow = 'weeknow'                 # Эта неделя
            monthnow = 'monthnow'               # Этот месяц
            recentupcoming = 'recentupcoming'   # Последние и ближайшие 60 дней
            custom = 'custom'                   # Пользовательский диапазон (5 дней до сегодня - сегодня спустя год)

        url = f'{URL}/calendar/export_execute.php?' \
              f'userid={userid}&' \
              f'authtoken={token}&' \
              f'preset_what={preset_what.all}&' \
              f'preset_time={preset_time.monthnow}'
        return url

    def get_access_info(self):
        access_info = self.user.call('core_calendar_get_calendar_access_information')
        return access_info

    def time_from_unix(self, epoch: int) -> str:
        """Converts the time from epoch to human readable time"""
        date = ctime(epoch).split()
        pprint(date)
        return f"{date[0]}, {date[2]} {date[1]}, {date[3][:-3]}"

    def time_to_unix(self, datetime):
        unix_time = int(datetime.timestamp())
        return unix_time