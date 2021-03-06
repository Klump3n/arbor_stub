#!/usr/bin/env python3
"""
A descriptive text.

"""
import argparse

from util.logging.logger import CoreLog as cl
from util.opt.greet import greeting


def parse_arguments():
    """
    Parse the command line arguments.

    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-l", "--log", help="set logging level",
                        choices=["quiet", "debug", "verbose", "info",
                                 "warning", "error", "critical"],
                        default="info")
    args = parser.parse_args()
    return args

def setup_loggers(logging_level):
    """
    Setup the logging level.

    """
    cl(logging_level)
    cl.verbose("starting logging")
    cl.verbose("logging level is set to {}".format(logging_level))
    if logging_level == "verbose" or logging_level == "debug":
        print()                 # newline

def greet():
    """
    Print a greeting.

    """
    print(greeting())

def main():
    """
    Main entry point.

    """
    args = parse_arguments()
    logging_level = args.log
    greet()
    setup_loggers(logging_level)

    cl.debug("DEBUG")
    cl.verbose("VERBOSE")
    cl.verbose_warning("VERBOSE_WARNING")
    cl.info("INFO")
    cl.warning("WARNING")
    cl.error("ERROR")
    cl.critical("CRITICAL")

if __name__ == "__main__":
    main()
