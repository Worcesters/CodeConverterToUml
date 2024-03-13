"""
This module provides a factory for creating parser instances.
"""
import importlib
from typing import Optional
from typing import List
from Definition.Language import Language
from ParserModule.Parser.Interface import IParser


class ParserFactory():
    """
    This class represents a factory for creating parser instances.
    """
    __parser_factory_instance: 'Optional[ParserFactory]' = None
    __language: 'Optional[Language]' = None
    __parser_instance: 'Optional[List[IParser]]' = None

    @classmethod
    def get_instance( cls, language: Language ):
        """
        Get an instance of the ParserFactory for a specific language.

        Args:
            language: The Language object for which the ParserFactory instance is needed.

        Returns:
            An instance of the ParserFactory.
        """
        if language is None and cls.__language is None:
            raise ValueError("La langue n'a pas été initialisée")

        if cls.__parser_factory_instance is None or cls.__language != language:
            cls.__parser_factory_instance = ParserFactory()
            cls.__language = language

        return cls.__parser_factory_instance

    @classmethod
    def get_parsers( cls ) -> List[IParser]:
        """
        Get the parsers for the specified language.

        Returns:
            List[IParser]: A list of instances of the parser for the specified language.
        """
        nom_module = ''
        parsers = None

        try:
            if cls.__language is not None :
                nom_module = f"ParserModule.Parser.{ cls.__language.name }"
                parsers = importlib.import_module( nom_module )

        except ModuleNotFoundError as exc:
            raise ImportError(f"Parser not found for the specified language. { parsers }") from exc

        structure_parser: IParser = parsers.StructureParser.StructureParser()
        method_parser: IParser = parsers.MethodParser.MethodParser()
        attribute_parser: IParser = parsers.AttributeParser.AttributeParser()

        parsers_list: List[IParser] = [
            structure_parser,
            method_parser,
            attribute_parser
        ]

        if cls.__parser_instance is None:
            cls.__parser_instance = parsers_list

        return cls.__parser_instance
