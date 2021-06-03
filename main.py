from ParserClass import Parser
from LexicalAnalyzerClass import LexicalAnalyzer
if __name__ == '__main__':
    sentence = input("Masukan kalimat: ")
    config = {
        'sentence': sentence,
        'parse_table_file': 'data/parser.csv',
        'lexical_transition_file': 'data/lexical.csv',
        'debug': False
    }
    l = LexicalAnalyzer(config)
    p = Parser(config)
    print(l.reading())
    print(p.reading())
