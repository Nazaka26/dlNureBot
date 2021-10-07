from pprint import pprint

from moodle_new import User


class Course:
    """Class for a single course.

    Example:
    >>> Course(name="Example course", shortname="example", categoryid=1)
    """

    def __init__(self, user: User, **kwargs):
        # """Get useful course page content"""
        self.user = user
        self.course_info = kwargs
        self.html_info = self.user.call('core_course_get_contents', courseid=self.course_info['id'])

    def get_html_content(self):
        return self.user.call('core_course_get_contents', courseid=self.course_info['id'])

    def get_modules(self):
        res = {}
        for section in self.html_info:
            for module in section['modules']:
                name = module['name']
                res[name] = module
        return res

    def get_course_module(self, module_id):
        module = self.user.call('core_course_get_course_module', cmid=module_id)
        module = module['cm']
        return module

