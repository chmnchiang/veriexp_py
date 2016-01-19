from .expression import Expression
from verilog.variable import ConstValue

class Constant(Expression):
    def __init__(self, rep):
        self.rep = rep

    def generate(self, context):
        return ConstValue(int(self.rep))
