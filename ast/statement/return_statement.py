from .statement import Statement
from verilog.statement import StoreReg
from verilog.variable import StateVariable, ConstValue

class ReturnStatement(Statement):
    def __init__(self, var):
        self.var = var

    def generate(self, context):
        context.A(
            StoreReg(context.ident_map['result'], 
                     self.var.generate(context))
        )
        context.A(
            StoreReg(context.ident_map['done'], 
                     ConstValue(1))
        )
        context.N(StateVariable(context.idle_state))

