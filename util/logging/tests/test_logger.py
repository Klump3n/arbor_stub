#!/usr/bin/env python3
"""
Test the string operations.

"""
import unittest

import sys
sys.path.append("..")
import logger
from logger import MyLog

class Test_Logger(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_logger_with_name(self):
        """create logger with name
        """
        log = logger.BaseLogger("SOMENAME")

        log.info("no")
        log.debug("no")

    def test_logger_without_name(self):
        """create logger without name
        """
        log = logger.BaseLogger()
        log.info("no")
        log.debug("no")

    def test_logger_with_name_setlevel(self):
        """create logger with name and logging level
        """
        log = logger.BaseLogger("SOMENAME", "debug")

        log.info("no")
        log.debug("no")

    def test_mylogger(self):
        """mylogger

        """
        with self.assertRaises(ValueError):
            MyLog.debug("hey")
        MyLog("debug")
        MyLog.info("hey")

    def test_mylogger_verbose(self):
        """mylogger

        """
        MyLog("debug")
        MyLog.verbose("hey")

if __name__ == '__main__':
    unittest.main(verbosity=2)

