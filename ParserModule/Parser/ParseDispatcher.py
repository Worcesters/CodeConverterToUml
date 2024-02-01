from Definition.Language import Language
class ParseDispatcher:
    def __init__(self, language: Language):
        self.language = language
        print('initialisation ParseDispatcher done')
        self.patterns = {
            Language.PHP: {
                'method_pattern': 
                    r"""
                        (?P<visibility>public|protected|private)?\s*
                        (?P<abstract>abstract\s+)?function\s+
                        (?P<method_name>\w+)\s*\(
                            (?P<method_params>.*?)
                        \)
                        (?:\s*:\s*(?P<return_type>\w+))?
                    """,
                'param_regex':
                    r"""
                        (?P<param_type>\w+)?\s*
                        \$(?P<param_name>\w+)
                    """,
                'attribute_pattern':
                    r"""
                        (?P<visibility>public|protected|private)?\s*
                        \$(?P<attribute_name>\w+)
                    """,
                'structure_pattern': 
                    r"""
                        (?P<type>class|interface|enum)\s+
                        (?P<name>\w+)\s*
                        (?:extends\s+(?P<extends>\w+)\s*)?
                        (?:implements\s+(?P<implements>[\w\s,]+))?
                    """
            },
            Language.PYTHON: {
                'method_pattern': r'python_method_regex',
                'params_pattern': r'python_params_regex',
                # Autres motifs pour Python
            },
            # Ajoutez d'autres langages et motifs ici
        }

    def get_pattern(self, pattern_key):
        language_patterns = self.patterns.get(self.language, {})
        return language_patterns.get(pattern_key)