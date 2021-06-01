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
        try:
            while(len(stack) > 0):
                top = stack[len(stack)-1]
                if self.debug:
                    print('[TOP]', top)
                    print('[SYMBOL]', symbol)
                if top in self.terminals:
                    if self.debug:
                        print('[FOUND] Terminal')
                    if top == symbol:
                        stack.pop()
                        idx_token += 1
                        symbol = self.tokens[idx_token]
                        if symbol == 'EOS':
                            if self.debug:
                                print('[ISI]', stack)
                            stack.pop()
                    else:
                        if self.debug:
                            print('[ERROR]')
                        break
                elif top in self.non_terminals:
                    if self.debug:
                        print('[FOUND] Non terminal')
                    if self.parse_table[(top, symbol)][0] != 'error':
                        stack.pop()
                        symbol_to_be_pushed = self.parse_table[(top, symbol)]
                        for i in range(len(symbol_to_be_pushed)-1, -1, -1):
                            stack.append(symbol_to_be_pushed[i])
                    else:
                        if self.debug:
                            print('[ERROR]')
                        break
                else:
                    if self.debug:
                        print('[ERROR]')
                    break
                if self.debug:
                    print('[STACK]', stack)
        except:
            if self.debug:
                print(['ERROR'])
        # Conclusion
        if symbol == 'EOS' and len(stack) == 0:
            print('[ACCEPT]', self.sentence, 'sesuai grammar')
        else:
            print('[ERROR]', self.sentence, 'tidak sesuai grammar')
