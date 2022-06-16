import sys
from nltk.stem.wordnet import WordNetLemmatizer


class LexicalAnalyzer:

    def __init__(self, input, verbs, adjectives, nouns, pronouns, prepositions, articles):
        self.input = input
        self.verbs = verbs
        self.adjectives = adjectives
        self.nouns = nouns
        self.pronouns = pronouns
        self.prepositions = prepositions
        self.articles = articles
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
        for word in self.input:
            if 'q' not in word.lower() or 'j' not in word.lower():
                # Noun Check
                if word.lower() in self.nouns:
                    self.add_noun_to_token(word)

                # Pronoun Check
                if word == "I":
                    self.add_pronoun_to_token(word)
                elif word.lower() in self.pronouns:
                    self.add_pronoun_to_token(word)

                # Verb Check
                if (word.lower() in self.verbs or WordNetLemmatizer().lemmatize(word, 'v') in self.verbs) and word.lower()[-2:] != "ly":
                    if self.tokens[-1][1].lower() in ['will', 'would', 'shall', 'should', 'am', 'is', 'are', 'was', 'were', 'has', 'have', 'had']:
                        self.add_verb_to_token(word)
                        continue
                    elif word not in self.checked and self.tokens[-1][0] != 'VERB':
                        self.add_verb_to_token(word)
                        continue
                    

                # Adjective Check
                if word.lower() in self.adjectives:
                    self.add_adjective_to_token(word)

                # Adverb Check
                if word.lower()[-2:] == "ly":
                    self.add_adverb_to_token(word)

                # Preposition Check
                if word.lower() in self.prepositions:
                    if self.tokens[-1][0] == 'VERB':
                        self.add_preposition_to_token(word)

                # Article Check
                if word.lower() in self.articles:
                    self.add_article_to_token(word)

                if (word.lower() not in self.nouns 
                        and word != "I"
                        and word.lower() not in self.pronouns 
                        and (word.lower() not in self.verbs or WordNetLemmatizer().lemmatize(word, 'v') not in self.verbs)
                        and word.lower() not in self.adjectives
                        and word.lower()[-2:] != "ly"
                        and word.lower() not in self.prepositions
                        and word.lower() not in self.articles):
                    print(f"The word '{word.lower()}' is not in the word list, please use another word.")
                    sys.exit()
            
            if 'q' in word.lower() or 'j' in word.lower():
                print(f"You have q or j in {word.lower()}, which is unknown in Human Language. Please try again.")
                sys.exit()
        
        return self.tokens