from .statement import Statement
from verilog.statement import StoreReg
from verilog.variable import StateVariable

class ReturnStatement(Statement):
    def __init__(self, value):
        self.value = value

    def generate(self, context):
        context.A(
            StoreReg(context.result_var, 
                     context.ident_map[self.value.name])
        )
        context.N(StateVariable(context.idle_state))

