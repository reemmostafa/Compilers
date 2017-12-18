from Scanner import Scanner
from Token import TokenType


class Parser:
    def __init__(self, scanner, input_path='', output_path=''):
        self._input_path = input_path
        self._output_path = output_path
        scanner.set_files(input_path, 'scanner_output.txt')
        self.tokens = scanner.run()
        self.current_token = None
        self.advance_input()

    def write_to_output_file(self,string):
        with open(self._output_path, 'a') as file:
            file.write(string + ' Found\n')

    def advance_input(self):
        try:
            self.current_token = self.tokens.__next__()
        except StopIteration:
            return False
        return True

    def start_parsing(self):
        self.program()

    def match(self, expected_token_value, expected_token_type):
        if expected_token_type == TokenType.ID:
            if expected_token_type == self.current_token.token_type:
                self.advance_input()
            else:
                raise ValueError('match error')
        else:
            if expected_token_value == self.current_token.string_value:
                self.advance_input()
            else:
                raise ValueError('match error')

    def program(self):
        self.stmt_sequence()
        self.write_to_output_file('Program')

    def stmt_sequence(self):
        self.statement()
        while self.current_token.string_value == ';':
            self.match(';', TokenType.SPSYMB)
            self.statement()
        self.write_to_output_file('Statement_Sequence')

    def statement(self):
        if self.current_token.string_value == 'if':
            self.if_stmt()
        elif self.current_token.string_value == 'repeat':
            self.repeat_stmt()
        elif self.current_token.token_type == TokenType.ID:
            self.assign_stmt()
        elif self.current_token.string_value == 'read':
            self.read_stmt()
        elif self.current_token.string_value == 'write':
            self.write_stmt()
        self.write_to_output_file('Statement')

    def if_stmt(self):
        pass

    def repeat_stmt(self):
        pass

    def assign_stmt(self):
        pass

    def read_stmt(self):
        pass

    def write_stmt(self):
        pass

    def exp(self):
        pass

    def simple_exp(self):
        pass

    def comparison_op(self):
        pass

    def term(self):
        pass

    def add_op(self):
        pass

    def factor(self):
        pass

    def mul_op(self):
        pass

if __name__ == "__main__":
    input_file = 'tiny_sample_code.txt'
    output_file = 'scanner_output.txt'
    scanner = Scanner()
    parser = Parser(scanner, input_file, output_file)
    parser.start_parsing()