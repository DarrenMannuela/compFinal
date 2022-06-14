import re
from nltk.stem.wordnet import WordNetLemmatizer


# tokens = []

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


# checked = []
# tokens = []
#
#
# def add_noun_to_token(word):
#     checked.append(word)
#     tokens.append(['NOUN', word])
#
#
# def add_pronoun_to_token(word):
#     checked.append(word)
#     tokens.append(['PRONOUN', word])
#
#
# def add_verb_to_token(word):
#     checked.append(word)
#     tokens.append(['VERB', word])
#
#
# def add_adjective_to_token(word):
#     checked.append(word)
#     tokens.append(['ADJECTIVE', word])
#
#
# def add_adverb_to_token(word):
#     checked.append(word)
#     tokens.append(['ADVERB', word])
#
#
# for word in input:
#     # Noun Check
#     if word.lower() in nouns:
#         add_noun_to_token(word)
#
#     # Pronoun Check
#     if word == "I":
#         add_pronoun_to_token(word)
#     elif word.lower() in pronoun:
#         add_pronoun_to_token(word)
#
#     # Verb Check
#     if (word.lower() or WordNetLemmatizer().lemmatize(word, 'v') in verbs) and word.lower()[-2:] != "ly" :
#         if word not in checked:
#             add_verb_to_token(word)
#
#     # Adjective Check
#     if word.lower() in adjectives:
#         add_adjective_to_token(word)
#
#     # Adverb Check
#     if word.lower()[-2:] == "ly":
#         add_adverb_to_token(word)
#
# print(tokens)


class LexicalAnalyzer:

    def __init__(self, input_list, verbs_list, adjectives_list,  nouns_list,  pronouns_list, prepositions_list):
        self.input_list = input_list
        self.verbs_list = verbs_list
        self.adjectives_list = adjectives_list
        self.nouns_list = nouns_list
        self.pronouns_list = pronouns_list
        self.prepositions_list = prepositions_list
        self.checked = []
        self.tokens = []

    def get_tokens(self):
        return self.tokens

    def add_noun_to_token(self, word: str):
        self.checked.append(word)
        self.tokens.append(['NOUN', word])

    def add_pronoun_to_token(self, word: str):
        self.checked.append(word)
        self.tokens.append(['PRONOUN', word])

    def add_verb_to_token(self, word: str):
        self.checked.append(word)
        self.tokens.append(['VERB', word])

    def add_adjective_to_token(self, word: str):
        self.checked.append(word)
        self.tokens.append(['ADJECTIVE', word])

    def add_adverb_to_token(self, word: str):
        self.checked.append(word)
        self.tokens.append(['ADVERB', word])

    def add_preposition_to_token(self, word: str):
        self.checked.append(word)
        self.tokens.append(['PREPOSITION', word])

    def analyze_input(self):
        for word in self.input_list:
            # Noun Check
            if word.lower() in self.nouns_list:
                self.add_noun_to_token(word)

            # Pronoun Check
            if word == "I":
                self.add_pronoun_to_token(word)
            elif word.lower() in self.pronouns_list:
                self.add_pronoun_to_token(word)

            # Verb Check
            if (word.lower() or WordNetLemmatizer().lemmatize(word, 'v') in self.verbs_list) and word.lower()[-2:] != "ly":
                if word not in self.checked and self.tokens[-1][0] != 'VERB':
                    self.add_verb_to_token(word)
                    continue

            # Adjective Check
            if word.lower() in self.adjectives_list:
                self.add_adjective_to_token(word)

            # Adverb Check
            if word.lower()[-2:] == "ly":
                self.add_adverb_to_token(word)

            # Preposition Check
            if word.lower() in self.prepositions_list:
                if self.tokens[-1][0] == 'VERB':
                    self.add_preposition_to_token(word)

        print(self.tokens)






