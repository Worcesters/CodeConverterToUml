from enum import Enum

class Language(Enum):
    PHP = "Php"
    PYTHON = "Python"
    JAVA = "Java"

    @staticmethod
    def from_value(value):
        for lang in Language:
            if lang.value == value:
                return lang
        return None

