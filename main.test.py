import unittest
from ParserClass import Parser
from LexicalAnalyzerClass import LexicalAnalyzer


class TestTubes(unittest.TestCase):

    def config(self, sentence):
        return {
            'sentence': sentence,
            'parse_table_file': 'data/parser.csv',
            'lexical_transition_file': 'data/lexical.csv',
            'debug': False
        }

    def test_subject(self):
        # test all subject
        s = ['father', 'mother', 'son']
        for i in s:
            config = self.config('{}'.format(i))
            l = LexicalAnalyzer(config)
            p = Parser(config)
            self.assertIn('[VALID]', l.reading(), 'Lexical salah')
            self.assertIn('[ERROR]', p.reading(), 'Parser salah')
            for j in s:
                config = self.config('{} {}'.format(i, j))
                l = LexicalAnalyzer(config)
                p = Parser(config)
                self.assertIn('[VALID]', l.reading(), 'Lexical salah')
                self.assertIn('[ERROR]', p.reading(), 'Parser salah')
                for k in s:
                    config = self.config('{} {} {}'.format(i, j, k))
                    l = LexicalAnalyzer(config)
                    p = Parser(config)
                    self.assertIn('[VALID]', l.reading(), 'Lexical salah')
                    self.assertIn('[ERROR]', p.reading(), 'Parser salah')

    def test_verb(self):
        # test all verb
        v = ['eat', 'meet', 'kick']
        for i in v:
            config = self.config('{}'.format(i))
            l = LexicalAnalyzer(config)
            p = Parser(config)
            self.assertIn('[VALID]', l.reading(), 'Lexical salah')
            self.assertIn('[ERROR]', p.reading(), 'Parser salah')
            for j in v:
                config = self.config('{} {}'.format(i, j))
                l = LexicalAnalyzer(config)
                p = Parser(config)
                self.assertIn('[VALID]', l.reading(), 'Lexical salah')
                self.assertIn('[ERROR]', p.reading(), 'Parser salah')
                for k in v:
                    config = self.config('{} {} {}'.format(i, j, k))
                    l = LexicalAnalyzer(config)
                    p = Parser(config)
                    self.assertIn('[VALID]', l.reading(), 'Lexical salah')
                    self.assertIn('[ERROR]', p.reading(), 'Parser salah')

    def test_object(self):
        # test all object
        o = ['salad', 'him', 'ball', 'bottle']
        for i in o:
            config = self.config('{}'.format(i))
            l = LexicalAnalyzer(config)
            p = Parser(config)
            self.assertIn('[VALID]', l.reading(), 'Lexical salah')
            self.assertIn('[ERROR]', p.reading(), 'Parser salah')
            for j in o:
                config = self.config('{} {}'.format(i, j))
                l = LexicalAnalyzer(config)
                p = Parser(config)
                self.assertIn('[VALID]', l.reading(), 'Lexical salah')
                self.assertIn('[ERROR]', p.reading(), 'Parser salah')
                for k in o:
                    config = self.config('{} {} {}'.format(i, j, k))
                    l = LexicalAnalyzer(config)
                    p = Parser(config)
                    self.assertIn('[VALID]', l.reading(), 'Lexical salah')
                    self.assertIn('[ERROR]', p.reading(), 'Parser salah')

    def test_subject_verb(self):
        # test all subject and verb
        s = ['father', 'mother', 'son']
        v = ['eat', 'meet', 'kick']
        for i in s:
            for j in v:
                config = self.config('{} {}'.format(i, j))
                l = LexicalAnalyzer(config)
                p = Parser(config)
                self.assertIn('[VALID]', l.reading(), 'Lexical salah')
                self.assertIn('[ERROR]', p.reading(), 'Parser salah')

    def test_subject_object(self):
        # test all subject and object
        s = ['father', 'mother', 'son']
        o = ['salad', 'him', 'ball', 'bottle']
        for i in s:
            for j in o:
                config = self.config('{} {}'.format(i, j))
                l = LexicalAnalyzer(config)
                p = Parser(config)
                self.assertIn('[VALID]', l.reading(), 'Lexical salah')
                self.assertIn('[ERROR]', p.reading(), 'Parser salah')

    def test_verb_object(self):
        # test all verb and object
        v = ['eat', 'meet', 'kick']
        o = ['salad', 'him', 'ball', 'bottle']
        for i in v:
            for j in o:
                config = self.config('{} {}'.format(i, j))
                l = LexicalAnalyzer(config)
                p = Parser(config)
                self.assertIn('[VALID]', l.reading(), 'Lexical salah')
                self.assertIn('[ERROR]', p.reading(), 'Parser salah')

    def test_subject_verb_object(self):
        # test all subject verb and object
        s = ['father', 'mother', 'son']
        v = ['eat', 'meet', 'kick']
        o = ['salad', 'him', 'ball', 'bottle']
        for i in s:
            for j in v:
                for k in o:
                    config = self.config('{} {} {}'.format(i, j, k))
                    l = LexicalAnalyzer(config)
                    p = Parser(config)
                    self.assertIn('[VALID]', l.reading(), 'Lexical salah')
                    self.assertIn('[ACCEPT]', p.reading(), 'Parser salah')

    def test_invalid_words(self):
        s = ['michael', 'yogi', 'akbar']
        v = ['read', 'write', 'speak']
        o = ['rock', 'laptop', 'router', 'keyboard']
        for i in s:
            for j in v:
                for k in o:
                    config = self.config('{} {} {}'.format(i, j, k))
                    l = LexicalAnalyzer(config)
                    p = Parser(config)
                    self.assertIn('[INVALID]', l.reading(), 'Lexical salah')
                    self.assertIn('[ERROR]', p.reading(), 'Parser salah')


if __name__ == '__main__':
    unittest.main()
