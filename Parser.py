from Scanner import Scanner


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

    def match(self):
        pass

    def program(self):
        self.stmt_sequence()
        self.write_to_output_file('Program')


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
    parser.start_parsing()