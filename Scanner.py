from enum import Enum
from Token import Token
from Token import TokenType

# enum for the states
class State(Enum):
    START = 1
    INCOMMENT = 2
    INNUM = 3
    INID = 4
    INASSIGN = 5
    DONE = 6

# set of reserved words
reserved_words = {'if', 'then', 'else', 'end', 'repeat', 'until', 'read', 'write'}
# set of special symbols
special_symbols = {'+', '-', '*', '/', '=', '<', '(', ')', ';', ':='}


class Scanner:
    def __init__(self,input_path='',output_path=''):
        # constructor gets the path input and output files
        # and set the current state to START state
        self._input_path = input_path
        self._output_path = output_path
        self._current_state = State.START

    def set_files(self,input_path,output_path):
        # use this function to change the path of input and output files
        self._input_path = input_path
        self._output_path = output_path

    def read_file(self):
        # open the input file and read it character by character
        with open(self._input_path) as file:
            while True:
                char = file.read(1)
                if not char:
                    break
                yield char

    def write_token(self,token,t_type):
        # write tokens to the output file
        tokentype = {TokenType.RESWORD: 'reserved word', TokenType.SPSYMB: 'special symbol',
                     TokenType.ID: 'identifier', TokenType.NUM: 'number'}

        with open(self._output_path, 'a') as file:
            file.write(token+' : '+tokentype[t_type]+'\n')

    def run(self) -> Token:
        # the main function of the scanner
        # check characters according to DFA and determines token types
        characters = self.read_file()
        end_of_file = False
        c = ''
        while not end_of_file:
            token = ''
            tokentype = None
            self._current_state = State.START

            while self._current_state != State.DONE:
                try:
                    if not c:
                        c = next(characters)
                except StopIteration:
                    end_of_file = True
                    break

                if self._current_state == State.START:
                    if c == '{':
                        self._current_state = State.INCOMMENT
                    elif c.isdigit():
                        self._current_state = State.INNUM
                        token += c
                        tokentype = TokenType.NUM
                    elif c.isalpha():
                        self._current_state = State.INID
                        token += c
                        tokentype = TokenType.ID
                    elif c == ':':
                        self._current_state = State.INASSIGN
                        token += c
                        tokentype = TokenType.SPSYMB
                    elif c in special_symbols:
                        self._current_state = State.DONE
                        token += c
                        tokentype = TokenType.SPSYMB
                    else:
                        self._current_state = State.START
                    c = ''

                elif self._current_state == State.INCOMMENT:
                    if c == '}':
                        self._current_state = State.START
                    c = ''

                elif self._current_state == State.INNUM:
                    if c.isdigit():
                        token += c
                        c = ''
                    else:
                        self._current_state = State.DONE

                elif self._current_state == State.INID:
                    if c.isalpha():
                        token += c
                        c = ''
                    else:
                        self._current_state = State.DONE

                elif self._current_state == State.INASSIGN:
                    self._current_state = State.DONE
                    if c == '=':
                        token += c
                        c = ''

            if tokentype == TokenType.ID and token in reserved_words:
                tokentype = TokenType.RESWORD
            self.write_token(token, tokentype)
            yield Token(token, tokentype)


if __name__ == "__main__":
    input_file = 'tiny_sample_code.txt'
    output_file = 'scanner_output.txt'
    scanner = Scanner(input_file, output_file)
    found = True
    g = scanner.run()
    while found:
        try:
            g.__next__()
        except StopIteration:
            break