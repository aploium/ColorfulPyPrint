# -*- coding: UTF-8 -*-
import sys

from .webqq_client import WebqqClient


class ExternalPrintBuffer:
    def __init__(self):
        self.buff = ''
        self.__console__ = sys.stdout

    def write(self, output_stream):
        self.buff += output_stream
        self.__console__.write(output_stream)

    def reset(self):
        sys.stdout = self.__console__
