from pprint import pprint

from moodle_new.Calendar import Calendar
from moodle_new.Timetable import Timetable
from moodle_new.User import User




nazar = User('nazar.kravchenko@nure.ua', '26Io2I2oo1')
nazar_calendar = Calendar(nazar)
timetable = Timetable()
# timetable.add(nazar_calendar.get_day_view(11, 10, 2021))
timetable.add(nazar_calendar.get_week_view(11, 10, 2021))


for time, course in timetable.items():
    print(time, course.course_info, sep='\t')
