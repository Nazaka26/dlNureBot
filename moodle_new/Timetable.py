from moodle_new.Calendar import Calendar


class Timetable:
    def __init__(self):
        self.timetable = {}

    def __iter__(self):
        return (x for x in self.timetable)

    def __len__(self):
        return len(self.timetable)

    def __repr__(self):
        return repr(self.timetable)

    def clear(self):
        return self.timetable.clear()

    def items(self):
        return self.timetable.items()

    # def add(self, user_calendar: Calendar):
    #     user_classes = user_calendar.get_current_day_view()
    #     for class_time, course in user_classes.items():
    #         self.timetable.update({class_time: course})


    def add(self, user_classes):
        for class_time, course in user_classes.items():
            self.timetable.update({class_time: course})


    def get_month(self):
        pass
    def get_week(self):
        pass
    def get_day(self):
        pass
    def get_today(self):
        pass