import logging
from logging import getLogger, StreamHandler, Formatter


def init_logging(name):
    logger = getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = Formatter('%(asctime)0.19s - %(module)s [%(levelname)s] %(message)s')

    handler = StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    fh = logging.FileHandler('error.log')
    fh.setLevel(logging.ERROR)
    fh.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(fh)
    logger.info("start logging")

    return logger
