from lexical_analyzer import LexicalAnalyzer

file = open('verbs.txt', 'r')
verbs = file.read().splitlines()
file.close()

file = open('adjectives.txt', 'r')
adjectives = file.read().splitlines()
file.close()

file = open('nouns.txt', 'r')
nouns = file.read().splitlines()
file.close()

file = open('pronouns.txt', 'r')
pronouns = file.read().splitlines()
file.close()

file = open('input.txt', 'r')
input = file.read().split()


file = open('preposition.txt', 'r')
prepositions = file.read().split()
file.close()


test = LexicalAnalyzer(input, verbs, adjectives, nouns, pronouns, prepositions)

test.analyze_input()


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.structure = []

    def check_structure(self):
        for token in self.tokens:
            self.structure.append(token[0])

    def print_structure(self):
        return self.structure


parse = Parser(test.get_tokens())

parse.check_structure()

print(parse.print_structure())


