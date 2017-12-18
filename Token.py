class Token:
    def __init__(self, token_type, string_value):
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