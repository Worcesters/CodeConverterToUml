from ParserModule.ParserManager import ParserManager
from ParserModule.Factory import ParserFactory
from Definition.Language import Language
from Registry.Registry import Registry
import os
import tkinter as tk
from tkinter import filedialog

def detect_language(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.py':
        return Language.PYTHON
    elif file_extension == '.php':
        return Language.PHP
    elif file_extension == '.java':
        return Language.JAVA
    else:
        return None

def main():
    try: 
        print( '┌──────────────────────────────────────────────────┐')
        print( '│                    Bienvenue                     │')
        print( '│     Début du script de séléction de fichiers     │')
        print( '└──────────────────────────────────────────────────┘')
        root = tk.Tk()
        root.withdraw()
        print('Lancement de l\'explorateur de fichier')
        print('└────────────────────────────────│')
        file_paths = filedialog.askopenfilenames(
            title="Sélectionner les fichiers à convertir en PlantUML",
            filetypes=[("Fichiers PHP, Python et Java", "*.php;*.py;*.java"), ("Tous les fichiers", "*.*")]
        )
        if not file_paths:
            error_message = (
                "┌──────────────────────────────────────────────────┐\n"
                "│                     ERREUR                       │\n"
                "│         Aucun fichier n'a été sélectionné.       │\n"
                "│     Veuillez sélectionner au moins un fichier.   │\n"
                "└──────────────────────────────────────────────────┘"
            )
            raise ValueError('\n' + error_message)
        
        print('Départ de la boucle de reconnaissance de la prise en charge du language')
        for file_path in file_paths:
            detected_language = detect_language(file_path)
            if detected_language:
                print(f"Langue détectée pour {file_path}: {detected_language}")
                print('├──├──├──├──├──├──├──│├──├──├──├──├──├──├──│')
                print('└───────────────────────────────────────────')
                
                print('initialisation ParserFactory')
                print('└────────────────────│')
                parser_factory = ParserFactory.get_instance(detected_language)
                print('ParserFactory -----> [DONE]')
                print('├──├──├──├──├──├──├──│├──├──├──├──├──├──├──│')
                print('└───────────────────────────────────────────')
                
                print('initialisation ParserManager')
                print('└────────────────────│')
                parser_manager = ParserManager()
                print('ParserManager -----> [DONE]')
                print('├──├──├──├──├──├──├──│├──├──├──├──├──├──├──│')
                print('└───────────────────────────────────────────')

                print('initialisation parser_manager.set_parser')
                print('└────────────────────│')
                parsers = parser_factory.get_parsers()
                parser_manager.set_parser(parsers)
                print('ParserManager set_parser() -----> [DONE]')
                print('├──├──├──├──├──├──├──│├──├──├──├──├──├──├──│')
                print('└───────────────────────────────────────────')
                
                print('Début du Parsage fichier(s)')
                print('└────────────────────────│')
                parser_manager.parse_file([file_path])
                print('├──├──├──├──├──├──├──│├──├──├──├──├──├──├──│')
                print('└───────────────────────────────────────────')
                
                print('Restitution des informations')
                print('└────────────────────────│')
                print(parser_manager.registry.get_root().get_children())
            else:
                print( '┌───────────────────────────────────────────────────┐')
                print( '│                     ERREUR                        │')
                print( '│        Langue non détectée pour le fichier        │')
                print( '└───────────────────────────────────────────────────┘')
                print(file_path)

    except Exception as e:
        print( '┌───────────────────────────────────────────────────┐')
        print( '│                     ERREUR                        │')
        print( '│            Une erreur est survenue                │')
        print( '└───────────────────────────────────────────────────┘')
        print(e)
        # Consignation de l'erreur 
        raise NotImplementedError("Une erreur non spécifiée a été détectée !")
    
if __name__ == "__main__":
    main()
