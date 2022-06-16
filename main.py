from lexical_analyzer import LexicalAnalyzer
from parser import Parser
from hl_generator import HumanLanguageGenerator


def main():
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

    lexer = LexicalAnalyzer(input, verbs, adjectives, nouns, pronouns, prepositions, articles)
    tokens = lexer.analyze_input()

    parser = Parser(tokens)
    parsed = parser.parse()

    hl_generator = HumanLanguageGenerator(parsed)
    hl_generator.generate_hl()


if __name__ == "__main__":
    main()