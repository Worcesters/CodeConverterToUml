import os
from Registry.Registry import Registry
from Registry.StructuralElement import StructuralElement

class ParserManager():
    def __init__( self ):
        self.parsers = []
        #TODO : Ajouter un objet de configuration pour la racine projet
        print('initialisation Registry')
        print('└────────────────────│')
        self.registry = Registry( StructuralElement.ProgramRegistry() )
        print('Registry -----> [DONE]')
        print('├──├──├──├──├──├──├──│├──├──├──├──├──├──├──│')
        print('└───────────────────────────────────────────')
    
    def set_parser( self, parsers ):
        for parser in parsers:
            self.parsers.append( parser )
    
    def reset_parsers( self ):
        self.parsers.clear()

    def parse_file( self, file_paths ):
        for file_path in file_paths:
            with open( file_path, 'r' ) as file:
                code = file.read()

            for line in code.split('\n'):
                for parser in self.parsers:
                    parser.parse( line, self.registry )

    def parse_files( self, file_paths ):
        for file_path in file_paths:
            self.parse_file( file_path )

    def parse_folders( self, folder_path ):
        file_paths = self.parse_files( folder_path )
        self.parse_files( file_paths )

    