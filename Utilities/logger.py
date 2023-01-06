import inspect
import logging


class logclass:

    def getthelog(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        fileHandler = logging.FileHandler("Log\\logfile2.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
