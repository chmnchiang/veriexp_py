from .statement import Statement
from verilog.variable import RegVariable

class StoreReg(Statement):
    def __init__(self, lhs, rhs):
        assert(isinstance(lhs, RegVariable))

        self.lhs = lhs
        self.rhs = rhs

    def code_gen(self, context):
        yield from self.lhs.code_gen(context)
        yield ' <= '
        yield from self.rhs.code_gen(context)
        yield ';\n'
