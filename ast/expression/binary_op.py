from .expression import Expression
from verilog.variable import BinaryOP as VBinaryOP

class BinaryOP(Expression):
    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs

    def generate(self, context):
        return VBinaryOP(
            self.lhs.generate(context),
            self.op,
            self.rhs.generate(context)
        )
