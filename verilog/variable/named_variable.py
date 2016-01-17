from .variable import Variable, IOType
from ..named import Named

class NamedVariable(Variable, Named):
    def __init__(self, name, length, io_type=IOType.normal):
        super().__init__(length)
        self.name = name
        self.io_type = io_type

    def code_gen(self, context):
        yield self.name

    def generate_declaration(self, context):
        yield self.name
