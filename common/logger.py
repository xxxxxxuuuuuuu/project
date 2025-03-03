import os
import sys
import logging
import functools
from termcolor import colored
import datetime
logger = None
@functools.lru_cache()
def create_logger(output_dir, name=''):
    # os.makedirs(("logs"), exist_ok=True)
    output_dir = os.path.join(os.getcwd(),"logs",output_dir)
    os.makedirs(output_dir, exist_ok=True)


    # cur_time =datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    # create formatter
    fmt = '[%(asctime)s %(name)s] : %(levelname)s %(message)s'
    color_fmt = colored('[%(asctime)s %(name)s]', 'green') + ': %(levelname)s %(message)s'

    # create console handlers for master process
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(
        logging.Formatter(fmt=color_fmt, datefmt='%Y-%m-%d %H:%M:%S'))
    logger.addHandler(console_handler)

    # create file handlers
    file_handler = logging.FileHandler(os.path.join(output_dir,"log.txt"), mode='a')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(fmt=fmt, datefmt='%Y-%m-%d %H:%M:%S'))
    logger.addHandler(file_handler)

    return logger,output_dir # logger obj , path of logger

def add_handler(obj):
    color_fmt = colored('[%(asctime)s %(name)s]', 'green') + ': %(levelname)s %(message)s'

    # create console handlers for master process
    console_handler = logging.StreamHandler(obj)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(
        logging.Formatter(fmt=color_fmt, datefmt='%Y-%m-%d %H:%M:%S'))
    logger.addHandler(console_handler)

def log_info(info):
    logger.info(info)


# logger = create_logger("log")
# print("初始化")
