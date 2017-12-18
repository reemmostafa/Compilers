from enum import Enum


# enum for the token types
class TokenType(Enum):
    RESWORD = 1
    SPSYMB = 2
    ID = 3
    NUM = 4


class Token:
    def __init__(self, string_value, token_type: TokenType):
        self._type = token_type
        self._stringValue = string_value

    @property
    def token_type(self):
        return self._type

    @property
    def string_value(self):
        return self._stringValue

    @token_type.setter
    def token_type(self, token_type):
        self._type = token_type

    @string_value.setter
    def string_value(self,string_value):
        self._stringValue = string_value
