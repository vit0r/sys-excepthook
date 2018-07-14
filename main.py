import logging
from logging.config import fileConfig
import sys
import traceback


def get_logger():
    fileConfig('logging.conf')
    logger = logging.getLogger(__file__)
    return logger

def logging_handler(type, exception, tb):
    traceback_repr = traceback.format_tb(tb)
    get_logger().exception('Uncaught exception: {} type: {} traceback: {}'.format(exception.message, type.message, traceback_repr))

def main():
    return 1/0

sys.excepthook = logging_handler

if __name__ == '__main__':
    print(main())