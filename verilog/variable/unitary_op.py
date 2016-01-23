from .temp_variable import TempVariable

class UnitaryOP(TempVariable):
    def __init__(self, op, rhs):
        super().__init__(rhs.length)
        self.op = op
        self.rhs = rhs

    def code_gen(self, context):
        yield '{}('.format(self.op)
        yield from self.rhs.code_gen(context)
        yield ')'
