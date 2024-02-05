from Definition.Language import Language
from ParserModule.Parser.Interface import IParser
#from ParserModule.Parser.Parser import Parser
from TreeModule.Tree import Tree
import importlib
from typing import Optional, Type

class ParserFactory():
    __parser_factory_instance: 'Optional[ParserFactory]' = None 
    __language: 'Optional[Language]' = None
    __parser_instance: 'Optional[IParser]' = None
    
    def __init__(self):
        pass
    
    @staticmethod
    def get_instance(cls, language: Language):
        if language is None and cls.__language is None:
            raise ValueError("La langue n'a pas été initialisée")
            
        if cls.__parser_factory_instance is None or cls.__language != language:
            cls.__parser_factory_instance = ParserFactory()
            cls.__language = language
            
        return cls.__parser_factory_instance
    
    @classmethod
    def get_parsers(cls) -> IParser:
        nom_module = f"ParserModule.Parser.{cls.language}"
        parsers = importlib.import_module(nom_module)
        
        print('Initialisation des parsers')
        print('└────────────────────────│')
        structure_parser = parsers.StructureParser.StructureParser()
        method_parser = parsers.MethodParser.MethodParser()
        attribute_parser = parsers.AttributeParser.AttributeParser()
        
        if cls.__parser_instance is None:
            cls.__parser_instance = IParser
          
        return [structure_parser, method_parser, attribute_parser]

