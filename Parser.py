from Scanner import Scanner


class Parser:
    def __init__(self, Scanner, input_path='',output_path=''):
        self._input_path = input_path
        self._output_path = output_path
        Scanner.set_files(input_path)
        self.tokens = Scanner.run()
        self.current_token = self.tokens.__next__()

    def advance_input(self):
        pass

    def start_parsing(self):
        self.program()

    def match(self):
        pass

    def program(self):
        pass

    def stmt_sequence(self):
        pass

    def statement(self):
        pass

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