#!/usr/bin/env python3
"""
A descriptive text.

"""
import argparse

from util.logging.logger import CoreLog as cl
from util.opt.greet import arbor_text

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
    cl.info("starting logging")
    cl.info("logging level is set to {}".format(logging_level))
    if not logging_level == "quiet":
        print()                 # newline

def greet():
    """
    Print a greeting.

    """
    print(arbor_text)

def main():
    """
    Main entry point.

    """
    args = parse_arguments()
    logging_level = args.log
    greet()
    setup_loggers(logging_level)

if __name__ == "__main__":
    main()
