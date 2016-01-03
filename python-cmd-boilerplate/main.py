#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from optparse import OptionParser
import logging
import re
import operator


VERSION = "v0.1"


def read_file(input_name):
    try:
        input_file = open(input_name, "r")
    except IOError:
        logging.info("Specified input file doesn't exist.")
        return

    input_file.close()

def main():
    parser = OptionParser(description='Sample Program description,
                          version=VERSION)
    parser.add_option('-i', '--input', default='sample.txt',
                      help='Sample Input File')
    parser.add_option('-v', '--verbose', action="store_true",
                      help='Print verbose')
    options, args = parser.parse_args()

    if options.verbose:
        lv = logging.DEBUG
    else:
        lv = logging.INFO
    logging.basicConfig(level=lv, format='[%(asctime)s] {%(levelname)s} %(message)s')


if __name__ == '__main__':
    exit(main())
