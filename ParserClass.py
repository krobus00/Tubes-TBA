import csv


class Parser:
    def __init__(self, config):
        self.sentence = config['sentence']
        self.parse_table_file = config['parse_table_file']
        self.debug = config['debug']
        # init
        self.tokens = self.sentence.lower().split()
        self.tokens.append('EOS')
        self.non_terminals = []
        self.terminals = []
        self.parse_table = {}
        # read file from csv file
        with open(self.parse_table_file) as file:
            reader = csv.reader(file, delimiter=';')
            for idx, val in enumerate(reader):
                if idx == 0:
                    self.terminals = val[1:-1]
                else:
                    for i, v in enumerate(val[1:-1]):
                        if len(v.split(' ')) > 0:
                            self.parse_table[(
                                val[0], self.terminals[i])] = v.split(' ')
                        else:
                            self.parse_table[(val[0], self.terminals[i])] = [v]
                    self.non_terminals.append(val[0])

    def reading(self):
        # stack init
        stack = ['#', 'S']
        # reading
        idx_token = 0
        symbol = self.tokens[idx_token]
        while(len(stack) > 0 and symbol in self.terminals):
            top = stack[len(stack)-1]
            if self.debug:
                print('[TOP]', top)
                print('[SYMBOL]', symbol)
            if top in self.terminals and top == symbol:
                if self.debug:
                    print('[FOUND] Terminal')
                stack.pop()
                idx_token += 1
                symbol = self.tokens[idx_token]
                if symbol == 'EOS':
                    if self.debug:
                        print('[ISI]', stack)
                    stack.pop()
            elif top in self.non_terminals and self.parse_table[(top, symbol)][0] != 'error':
                if self.debug:
                    print('[FOUND] Non terminal')
                stack.pop()
                symbol_to_be_pushed = self.parse_table[(top, symbol)]
                for i in range(len(symbol_to_be_pushed)-1, -1, -1):
                    stack.append(symbol_to_be_pushed[i])
            else:
                break
            if self.debug:
                print('[STACK]', stack)
        # Conclusion
        if symbol == 'EOS' and len(stack) == 0:
            return '[ACCEPT] {} sesuai grammar'.format(self.sentence)
        else:
            return '[ERROR] {} tidak sesuai grammar'.format(self.sentence)
