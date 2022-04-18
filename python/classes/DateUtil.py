# -*- coding: utf-8 -*-
__author__ = 'zhaohui'

import datetime
import time
from dateutil.relativedelta import relativedelta


class DateUtil:
    def __init__(self):
        pass

    @staticmethod
    def get_today():
        return datetime.date.today()

    @staticmethod
    def get_before_day(day):
        return datetime.date.today() - datetime.timedelta(days=day)

    @staticmethod
    def get_time():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def get_time_stamp():
        return int(time.time())


if __name__ == '__main__':
    pass


