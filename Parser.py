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
        self.match('if', TokenType.RESWORD)
        self.exp()
        self.match('then', TokenType.RESWORD)
        self.stmt_sequence()
        if self.current_token.string_value == 'else':
            self.match('else', TokenType.RESWORD)
            self.stmt_sequence()
        self.match('end', TokenType.RESWORD)
        self.write_to_output_file('IF_Statement')

    def repeat_stmt(self):
        self.match('repeat', TokenType.RESWORD)
        self.stmt_sequence()
        self.match('until', TokenType.RESWORD)
        self.exp()
        self.write_to_output_file('Repeat_Statement')

    def assign_stmt(self):
        self.match('', TokenType.ID)
        self.match(':=', TokenType.SPSYMB)
        self.exp()
        self.write_to_output_file('Assignment_Statement')

    def read_stmt(self):
        self.match('read', TokenType.RESWORD)
        self.match('', TokenType.ID)
        self.write_to_output_file('Read_Statement')

    def write_stmt(self):
        self.match('write', TokenType.RESWORD)
        self.exp()
        self.write_to_output_file('Write_Statement')

    def exp(self):
        self.simple_exp()
        if self.current_token.string_value == '<' or self.current_token.string_value == '=':
            self.comparison_op()
            self.simple_exp()
        self.write_to_output_file('Expression')

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
    output_file = 'parser_output.txt'
    scanner = Scanner()
    parser = Parser(scanner, input_file, output_file)
    parser.start_parsing()