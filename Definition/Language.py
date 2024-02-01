from enum import Enum

class Language(Enum):
    PHP = "Php"
    PYTHON = "Python"
    JAVA = "Java"

    def from_value(value):
        print(value)
        for lang in Language:
            if lang.value == value:
                return lang
        return None

# Ajouter un print ou un assert pour confirmer
print("Méthode from_value définie dans Language")

