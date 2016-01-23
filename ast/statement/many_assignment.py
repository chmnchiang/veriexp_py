from .statement import Statement
from verilog.statement import StoreReg

class ManyAssignment(Statement):
    def __init__(self, lhs_list, rhs_list):
        assert len(lhs_list) == len(rhs_list)
        self.lhs_list = lhs_list
        self.rhs_list = rhs_list

    def generate(self, context):
        for x, y in zip(self.lhs_list, self.rhs_list):
            context.A(StoreReg(x.generate(context), 
                               y.generate(context)))
        context.N(context.next_state)
