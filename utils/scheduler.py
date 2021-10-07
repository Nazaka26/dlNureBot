import logging
from datetime import datetime
from datetime import timedelta
from random import randrange

from aiogram import Dispatcher
from apscheduler.triggers.combining import AndTrigger
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.interval import IntervalTrigger
from loader import scheduler
from moodle_new.Calendar import Calendar
from moodle_new.Timetable import Timetable
from moodle_new.User import User
from repository.UserRepository import UserRepository


logger = logging.getLogger(__name__)


async def add_random_delay(time, max_delay):
    rand_value = randrange(max_delay)
    time_delay = timedelta(seconds=rand_value)
    return time + time_delay


async def get_users_timetable() -> Timetable:
    """
    Gets all today's events for each of stored_users.
    :return: Timetable
    """
    stored_users = await UserRepository.all()
    timetable = Timetable()
    for stored_user in stored_users:  # todo: incapsulate in moodle module
        moodle_user = User(stored_user.login, stored_user.pswd)
        moodle_calendar = Calendar(moodle_user)
        timetable.add(moodle_calendar.get_upcoming_events())
    return timetable


async def jopa():
    print('jopa')


async def schedule_users_attendance():
    """
    Adds to schedule all users today's events.
    :return:
    """
    timetable = await get_users_timetable()
    logger.info(f'{len(timetable)} events need to be scheduled.')
    for time, course in timetable.items():
        # job = jopa
        # trigger = AndTrigger([DateTrigger(run_date=time),
        #                       IntervalTrigger(jitter=1)])
                # scheduler.add_job(job, trigger='interval', seconds=2)

        job = course.user.check_attendance_by
        time = await add_random_delay(time, max_delay=120)
        scheduler.add_job(job, trigger='date', run_date=time, args=[course])


async def update_scheduler():
    """
    Updates scheduler according to today's events.
    :return:
    """
    # scheduler.remove_all_jobs()

    await schedule_users_attendance()


async def run_jobs():
    """
    Starts all scheduler jobs.
    :return:
    """
    job = update_scheduler
    scheduler.add_job(job, trigger='cron', day=1, hour=5)
    await update_scheduler()


# fv


async def send_scheduled(dp: Dispatcher):
    stored_users = await UserRepository.all()
    for stored_user in stored_users:
        # todo send message to a user by chat_id
        id = stored_user.chat_id


async def view_jobs():
    jobs = scheduler.get_jobs()
    for job in jobs:
        print(job.next_run_time)
    print(jobs)
    return jobs




