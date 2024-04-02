"""
Module that contains the definition of the ParserManager class.

This class is in charge of creating and storing the parsers that will be
used to parse the code. It also provides a method to parse all the files
of a given project.
"""
import os
from typing import List

from Registry.Registry import Registry
from Registry.StructuralElement import RegistryProgram


# --------------------------------------------------------------------------- #
# Class definition
# --------------------------------------------------------------------------- #


class ParserManager():
    """
    Manager of parsers.

    This class is in charge of creating and storing the parsers that will be
    used to parse the code. It also provides a method to parse all the files
    of a given project.
    """
    def __init__( self ):
        self.parsers = []
        #TODO : Ajouter un objet de configuration pour la racine projet
        print('initialisation Registry')
        print('└────────────────────│')
        self.registry = Registry( RegistryProgram() )
        print('Registry -----> [DONE]')
        print('├──├──├──├──├──├──├──│├──├──├──├──├──├──├──│')
        print('└───────────────────────────────────────────')

    def set_parser( self, parsers ):
        """
        Add the parsers to the manager

        Args:
            parsers (list): The list of parsers to add
        """

        self.reset_parsers()

        for parser in parsers:
            self.parsers.append( parser )

    def reset_parsers(self):
        """
        Remove all the parsers from the manager.
        """
        self.parsers.clear()

    def parse_file( self, file_paths ):
        """
        Parse all the files in the given list

        Args:
            file_paths (list): A list of file paths to parse
        """
        for file_path in file_paths:
            with open(file_path, mode="r", encoding="utf-8") as file:
                code = file.read()

            for line in code.split('\n'):
                # Iterate over all the parsers and parse the current file line
                for parser in self.parsers:
                    # Parse the line with the current parser
                    parser.parse( line, self.registry )

    def parse_files(self, file_paths):
        """
        Parse all the files in the given list

        Args:
            file_paths (list): A list of file paths to parse
        """
        # Iterate over all the files in the list and parse them
        for file_path in file_paths:
            with open(file_path, mode="r", encoding="utf-8") as file:
                code = file.read()

            for line in code.split('\n'):
                # Iterate over all the parsers and parse the current file line
                for parser in self.parsers:
                    # Parse the line with the current parser
                    parser.parse(line, self.registry)
        for file_path in file_paths:
            self.parse_file( file_path )

    def parse_folders(self, folder_path: str) -> None:
        '''
        Parse all the files in the given folder path

        Args:
            folder_path (str): The path of the folder to parse
        '''
        # Get all the file paths in the given folder
        file_paths: List[str] = []
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_paths.append(os.path.join(root, file))

        self.parse_files(file_paths)
