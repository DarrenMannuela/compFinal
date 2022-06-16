import sys


class Parser:

    def __init__(self, tokens):
        self.ast = {'VariableDeclaration': []}
        self.type_structure = []
        self.value_structure = []
        self.tokens = tokens
        self.count = 1
        self.y = 0

    def parse(self):
        for x in range(0, len(self.tokens)):
            token_type = self.tokens[x][0]
            token_value = self.tokens[x][1]
            self.type_structure.append(token_type)
            self.value_structure.append(token_value)
            # print(self.type_structure)

        # Simple Past and Present
        if (self.type_structure == ['PRONOUN', 'VERB', 'ARTICLE', 'NOUN'] 
                or self.type_structure == ['PRONOUN', 'VERB', 'NOUN', 'NOUN'] 
                or self.type_structure == ['PRONOUN', 'VERB', 'NOUN'] 
                or self.type_structure == ['PRONOUN', 'VERB', 'PRONOUN', 'NOUN']
                or self.type_structure == ['ARTICLE', 'NOUN', 'VERB', 'ADVERB']):
            for i in range(len(self.value_structure)):
                self.ast['VariableDeclaration'].append({self.type_structure[i].lower(): self.value_structure[i]})
        
        # Future Tense
        elif ((self.type_structure == ['PRONOUN', 'VERB', 'VERB', 'ARTICLE', 'NOUN'] and (self.value_structure[1].lower() == 'will' or self.value_structure[1].lower() == 'shall'))
                or (self.type_structure == ['PRONOUN', 'VERB', 'VERB', 'ARTICLE', 'ADJECTIVE', 'NOUN'] and (self.value_structure[1].lower() == 'will' or self.value_structure[1].lower() == 'shall'))
                or (self.type_structure == ['PRONOUN', 'VERB', 'VERB', 'NOUN'] and (self.value_structure[1].lower() == 'will' or self.value_structure[1].lower() == 'shall'))
                or (self.type_structure == ['PRONOUN', 'VERB', 'VERB'] and (self.value_structure[1].lower() == 'will' or self.value_structure[1].lower() == 'shall'))):
            for i in range(len(self.value_structure)):
                self.ast['VariableDeclaration'].append({self.type_structure[i].lower(): self.value_structure[i]})
        
        # Present Continuous
        elif ((self.type_structure == ['PRONOUN', 'VERB', 'VERB', 'ARTICLE', 'NOUN'] and (self.value_structure[1].lower() == 'am' or self.value_structure[1].lower() == 'is' or self.value_structure[1].lower() == 'are'))
                or (self.type_structure == ['PRONOUN', 'VERB', 'VERB', 'NOUN'] and (self.value_structure[1].lower() == 'am' or self.value_structure[1].lower() == 'is' or self.value_structure[1].lower() == 'are'))
                or (self.type_structure == ['PRONOUN', 'VERB', 'VERB', 'PRONOUN', 'VERB', 'PREPOSITION', 'VERB'] and (self.value_structure[1].lower() == 'am' or self.value_structure[1].lower() == 'is' or self.value_structure[1].lower() == 'are'))):
            for i in range(len(self.value_structure)):
                self.ast['VariableDeclaration'].append({self.type_structure[i].lower(): self.value_structure[i]})

        # Past Continuous
        elif ((self.type_structure == ['PRONOUN', 'VERB', 'VERB', 'ARTICLE', 'NOUN'] and (self.value_structure[1].lower() == 'was' or self.value_structure[1].lower() == 'were'))
                or (self.type_structure == ['PRONOUN', 'VERB', 'VERB', 'NOUN'] and (self.value_structure[1].lower() == 'was' or self.value_structure[1].lower() == 'were'))
                or (self.type_structure == ['PRONOUN', 'VERB', 'VERB', 'PRONOUN', 'VERB', 'PREPOSITION', 'VERB'] and (self.value_structure[1].lower() == 'was' or self.value_structure[1].lower() == 'were'))):
            for i in range(len(self.value_structure)):
                self.ast['VariableDeclaration'].append({self.type_structure[i].lower(): self.value_structure[i]})

        else:
            print("Unknown sentence structure or sentence structure not implemented, please try another structure.")
            sys.exit()
        return self.ast