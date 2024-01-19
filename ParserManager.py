from Parser import MethodParser, StructureParser, AttributeParser
import Registery

class ParserManager():
    def __init__(self):
        self.registery = Registery()
        self.current_class = None
        self.parsers = [
            StructureParser(self.registery,  self.current_class),
            MethodParser(self.registery,  self.current_class),
            AttributeParser(self.registery,  self.current_class)
        ]

    def parse(self, line: str):
        # Utiliser le code complet du fichier pour une ligne donnée
        with open('chemin/vers/votre/fichier.php', 'r') as file:
            code = file.read()

        for parser in self.parsers:
            parser.parse(line, code)