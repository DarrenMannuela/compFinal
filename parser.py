from lexical_analyzer import LexicalAnalyzer


file = open('word_lists/verbs.txt', 'r')
verbs = file.read().splitlines()
file.close()

file = open('word_lists/adjectives.txt', 'r')
adjectives = file.read().splitlines()
file.close()

file = open('word_lists/nouns.txt', 'r')
nouns = file.read().splitlines()
file.close()

file = open('word_lists/pronouns.txt', 'r')
pronouns = file.read().splitlines()
file.close()

file = open('word_lists/prepositions.txt', 'r')
prepositions = file.read().split()
file.close()

file = open('word_lists/articles.txt', 'r')
articles = file.read().split()
file.close()

file = open('input.txt', 'r')
input = file.read().split()

class Parser:
    def __init__(self):
        self.ast = {'VariableDeclaration': []}

    def get_lexer(self):
        lexer = LexicalAnalyzer().analyze_input()
        return lexer

    def parse(self):
        lex = self.get_lexer()
        for x in range(0, len(lex)):
            token_type = lex[x][0]
            token_value = lex[x][1]

            if x == 0 and token_type == 'PRONOUN':
                self.ast['VariableDeclaration'].append({'pronoun': token_value})
            elif x == 1 and token_type == 'VERB':
                self.ast['VariableDeclaration'].append({'verb': token_value})
            elif x == 2 and token_type == 'ARTICLE':
                self.ast['VariableDeclaration'].append({'article': token_value})
            elif x == 2 and token_type == 'NOUN':
                self.ast['VariableDeclaration'].append({'noun': token_value})
            elif x == 3 and token_type == 'NOUN':
                self.ast['VariableDeclaration'].append({'noun': token_value})
        return self.ast

parser = Parser()
print(parser.parse())