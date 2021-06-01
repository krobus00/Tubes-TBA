import string
import csv


class LexicalAnalyzer:
    def __init__(self, config):
        self.sentence = config['sentence']
        self.debug = config['debug']
        self.lexical_transition_file = config['lexical_transition_file']
        self.input_string = config['sentence'].lower() + '#'
        self.alphabet_list = list(string.ascii_lowercase)
        self.state_list = []
        self.transition_table = {}
        self.update_transition_table = {}
        with open(self.lexical_transition_file) as file:
            reader = csv.reader(file, delimiter=';')
            for val in reader:
                if val[0] not in self.state_list:
                    self.state_list.append(val[0])
                action = val[1].split(' ')
                action[0] = action[0].replace('spasi', ' ')
                self.update_transition_table[(val[0], action[0])] = action[1]
        for state in self.state_list:
            for aplhabet in self.alphabet_list:
                self.transition_table[(state, aplhabet)] = 'error'
            self.transition_table[(state, '#')] = 'error'
            self.transition_table[(state, ' ')] = 'error'
        for i in self.update_transition_table:
            self.transition_table[i] = self.update_transition_table[i]

    def reading(self):
        idx_char = 0
        state = 'q1'
        current_token = ''
        while state != 'accept' and idx_char < len(self.sentence):
            current_char = self.input_string[idx_char]
            current_token += current_char
            state = self.transition_table[(state, current_char)]
            if (state == 'q9' or state == 'q19' or state == 'q34') and self.debug:
                print('[VALID] current token :', current_token)
                current_token = ''
            if state == 'error' and self.debug:
                print('[INVALID] current token :', current_token)
                break
            idx_char += 1
        if state == 'accept':
            print("[VALID]", self.sentence)
        else:
            print("[INVALID]", self.sentence)
