class Word:
    def __init__(self, english, tenandi, part, definition):
        self.english = english
        self.tenandi = tenandi
        self.part = part
        self.definition = definition

    def get_english(self):
        return self.english
    
    def get_tenandi(self):
        return self.tenandi
    
    def get_part(self):
        return self.part
    
    def get_definition(self):
        return self.definition
    
class Verb(Word):
    def __init__(self, english, tenandi, definition,):
        super().__init__(english, tenandi, definition)
    
    