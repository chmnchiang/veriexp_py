from .temp_variable import TempVariable

class BinaryOP(TempVariable):
    def __init__(self, lhs, op, rhs):
        super().__init__(max(lhs.length, rhs.length))
        self.lhs = lhs
        self.op = op
        self.rhs = rhs

    def code_gen(self, context):
        yield '('
        yield from self.lhs.code_gen(context)
        yield ') {} ('.format(self.op)
        yield from self.rhs.code_gen(context)
        yield ')'
