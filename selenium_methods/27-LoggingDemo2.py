import logging

FORMAT = '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig(filename="C://Users//seker//Documents//seleniumLogs//test.log",
                    format=FORMAT,
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    )

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is a debug message")
logger.info("This is a info message")
logger.warning("This is a warning message")
logger.error("This is a error message")
logger.critical("This is a critical message")