import logging

FORMAT = '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig(filename="C://Users//seker//Documents//seleniumLogs//test.log",
                    format=FORMAT,
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG
                    )

logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")
