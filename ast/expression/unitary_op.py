from .expression import Expression
from verilog.variable import UnitaryOP as VUnitaryOP

class UnitaryOP(Expression):
    def __init__(self, op, rhs):
        self.op = op
        self.rhs = rhs

    def generate(self, context):
        return VUnitaryOP(
            self.op,
            self.rhs.generate(context)
        )
