import logging
import logging.handlers
import os


def setup_logger(level=logging.INFO):
    logger = logging.getLogger("ftg_adaptive_response_logger")
    logger.propagate = False
    logger.setLevel(level)
    file_handler = logging.handlers.RotatingFileHandler(
        os.environ["SPLUNK_HOME"] + "/var/log/splunk/ftg_adaptive_response.log",
        maxBytes=25000000,
        backupCount=5,
    )
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger