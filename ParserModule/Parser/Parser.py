from abc import ABC, abstractmethod, abstractclass
from Registry.RegistryModule import Registry
from ParserModule.Parser.Interface import IParser
from typing import Optional, Type


@abstractclass
class Parser(IParser):

    def __init__(self):
        pass