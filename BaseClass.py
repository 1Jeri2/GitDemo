import inspect
import logging


class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        #to print the method name from which the parent class is called
        #logger = logging.getLogger(__name__)
        # at runtime capture the filename and prints the test_logging.py in logs
        # if not given print root istead od of filename
        # method to create a logger object

        filehandler = logging.FileHandler("fileinfo.log")  # to tell the location and the filename for logs
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        # s for string others for format
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)  # to fetch filehandler object

        logger.setLevel(logging.DEBUG)  # skips the debug level and print frm other levels in level order
        return logger