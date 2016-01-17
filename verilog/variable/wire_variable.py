from .named_variable import NamedVariable
from .variable import IOType

class WireVariable(NamedVariable):
    def __init__(self, name, length, io_type=IOType.normal):
        super().__init__(name, length, io_type)

    def generate_declaration(self, context):
        if self.length > 1:
            yield "{} wire [{}:0] {};\n".format(
                self.io_type,
                self.length-1,
                self.name)
        else:
            yield "{} wire {};\n".format(
                self.io_type,
                self.name)

