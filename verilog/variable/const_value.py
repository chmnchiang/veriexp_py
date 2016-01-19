from .variable import Variable

class ConstValue(Variable):
    def __init__(self, val):
        super().__init__(val.bit_length())
        self.val = val

    def code_gen(self, context):
        yield str(self.val)
