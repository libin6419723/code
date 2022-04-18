# -*- coding: utf-8 -*-

import logging
import datetime

class Logger:
    loggers = {} 

    def __init__(self):
        pass

    @staticmethod
    def getLogger(name):
        name = name + '_' + datetime.datetime.now().strftime('%Y%m%d')
        if not name in Logger.loggers:
            create_dt = datetime.date.today()
            # 创建一个logger
            logger = logging.getLogger(name)
            logger.setLevel(logging.DEBUG)

            # 创建一个handler，用于写入日志文件
            fh = logging.FileHandler('../logs/' + name + '.log')
            fh.setLevel(logging.INFO)

            # 定义handler的输出格式
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)

            # 给logger添加handler
            logger.addHandler(fh)
            Logger.loggers[name] = logger;
            
        else: 
            logger = Logger.loggers[name]
        return logger
