"""Class to handle custom user exceptions."""
from lib.logger.logging import Logger

LOG_ERROR = Logger(loggername=__name__, loglevel='ERROR').log
LOG_CRITICAL = Logger(loggername=__name__, loglevel='CRITICAL').log
LOG_WARNING = Logger(loggername=__name__, loglevel='WARNING').log


class ToothlessException(Exception):
    """Custom User Exception class."""
    def __init__(self, error_msg, log_level):
        if log_level == 'ERROR':
            LOG_ERROR.error(error_msg)
        if log_level == 'WARNING':
            LOG_WARNING.error(error_msg)
        if log_level == 'CRITICAL':
            LOG_CRITICAL.error(error_msg)
        super(ToothlessException, self).__init__(error_msg)

class TestError(ToothlessException):
    """Error class."""
    def __init__(self, err_msg):
        super(TestError, self).__init__(err_msg)

class TestWarning(ToothlessException):
    """Warning class."""
    def __init__(self, err_msg):
        super(TestWarning, self).__init__(err_msg)

class TestFail(ToothlessException):
    """Fail class."""
    def __init__(self, err_msg):
        super(TestFail, self).__init__(err_msg)
