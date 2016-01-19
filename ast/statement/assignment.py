from .statement import Statement
from verilog.statement import StoreReg

class Assignment(Statement):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def generate(self, context):
        context.A(StoreReg(self.lhs.generate(context), 
                           self.rhs.generate(context)))
        context.N(context.next_state)
