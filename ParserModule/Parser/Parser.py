from abc import ABC, abstractmethod
from Registry.Registry import Registry
from ParserModule.Parser.Interface import IParser
from typing import Optional, Type


class Parser(IParser):

    def __init__(self):
        pass