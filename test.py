# -*- coding:utf-8 -*-
import sys
import os

from aioquant import quant


def initialize():
    print("Hello")
    pass

if __name__ == "__main__":
    config_file = sys.argv[1]
    quant.start(config_file, initialize)
