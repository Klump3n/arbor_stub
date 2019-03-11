#!/usr/bin/env python3
import logging


class BaseLogger(logging.Logger):
    """
    A simple logging class.

    """
    def __init__(self, name="", logging_level="info"):
        """
        Setup the base logging class.

        Set name and logging level.

        """
        super().__init__(name)

        if logging_level == "quiet":
            logging_level = logging.NOTSET
        elif logging_level == "debug":
            logging_level = logging.DEBUG
        elif logging_level == "verbose":
            logging_level = 15  # custom
        elif logging_level == "info":
            logging_level = logging.INFO
        elif logging_level == "warning":
            logging_level = logging.WARNING
        elif logging_level == "error":
            logging_level = logging.ERROR
        elif logging_level == "critical":
            logging_level = logging.CRITICAL

        # add a verbose setting
        logging.addLevelName(15, "VERBOSE")

        if not name == "":
            fmt = "[%(asctime)s; %(name)s] (%(levelname)s): %(message)s"
        else:
            fmt = "[%(asctime)s] (%(levelname)s): %(message)s"

        fmt_date = "%d.%m.%Y %T"
        formatter = logging.Formatter(fmt, fmt_date)
        handler = logging.StreamHandler()
        handler.setLevel(logging_level)
        handler.setFormatter(formatter)

        self.setLevel(logging_level)
        self.addHandler(handler)

        if logging_level == logging.NOTSET:
            logging.disable()


class LogWrapper(object):
    _wrapper_instance = None
    def __new__(cls, name, level):
        cls._wrapper_instance = BaseLogger(name, level)
        return cls

    @classmethod
    def _check_inst(cls):
        """
        Check for class instantiation.

        """
        if not cls._wrapper_instance:
            raise ValueError("LogWrapper not instantiated")

    @classmethod
    def debug(cls, msg):
        cls._check_inst()
        cls._wrapper_instance.debug(msg)

    @classmethod
    def verbose(cls, msg):
        if not cls._wrapper_instance:
            raise ValueError("LogWrapper not instantiated")
        cls._wrapper_instance.log(15, msg)

    @classmethod
    def info(cls, msg):
        cls._check_inst()
        cls._wrapper_instance.info(msg)

    @classmethod
    def warning(cls, msg):
        cls._check_inst()
        cls._wrapper_instance.warning(msg)

    @classmethod
    def error(cls, msg):
        cls._check_inst()
        cls._wrapper_instance.error(msg)

    @classmethod
    def critical(cls, msg):
        cls._check_inst()
        cls._wrapper_instance.critical(msg)


class CoreLog(LogWrapper):
    _my_instance = None
    def __new__(cls, level):
        if not cls._my_instance:
            cls._my_instance = LogWrapper("Core", level)
        return cls
