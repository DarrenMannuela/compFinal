from nltk.stem.wordnet import WordNetLemmatizer


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

class LexicalAnalyzer:

    def __init__(self):
        self.input_list = input
        self.verbs_list = verbs
        self.adjectives_list = adjectives
        self.nouns_list = nouns
        self.pronouns_list = pronouns
        self.prepositions_list = prepositions
        self.articles_list = articles
        self.checked = []
        self.tokens = []

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

    def add_article_to_token(self, word: str):
        self.checked.append(word)
        self.tokens.append(['ARTICLE', word])

    def analyze_input(self):
        for word in self.input_list:
            if 'q' or 'j' not in word.lower():
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

                # Article Check
                if word.lower() in self.articles_list:
                    self.add_article_to_token(word)
            else:
                return "You have q and j in your word, which is unknown in Human Language. Please try again."
        return self.tokens

test = LexicalAnalyzer()
# print(test.analyze_input())