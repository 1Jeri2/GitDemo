import logging
#just for git purpose

#changes made for gitpurpose ny GitX
def test_loggingDemo():
    logger = logging.getLogger(__name__) #at runtime capture the filename and prints the test_logging.py in logs
    #if not given print root istead od of filename
    #method to create a logger object

    filehandler = logging.FileHandler("fileinfo.log") #to tell the location and the filename for logs
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    #s for string others for format
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler) #to fetch filehandler object

    logger.setLevel(logging.DEBUG) #skips the debug level and print frm other levels in level order
    logger.debug("A debug statement is executed")
    logger.info("information not releated to pass/fail")
    logger.warning("any alerts eg:negative amount deduted")
    logger.error("error info")
    logger.debug("A debug statement is executed")
    logger.critical("critical conditions in code")


#logging levels #>debug
                #>info
                #>warning
                #>error
                #>critical
