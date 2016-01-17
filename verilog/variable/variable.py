from ..node import Node
from enum import Enum

class IOType(Enum):
    normal = 0
    input  = 1
    output = 2

    def __str__(self):
        if self == IOType.normal:
            return ''
        elif self == IOType.input:
            return 'input'
        elif self == IOType.output:
            return 'output'

class Variable(Node):
    def __init__(self, length, io_type=IOType.normal):
        self.length = length
        self.io_type = io_type
