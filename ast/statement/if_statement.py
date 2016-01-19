from .statement import Statement
from verilog.variable import Mux, StateVariable

class IfStatement(Statement):
    def __init__(self, cond_var, block):
        self.cond_var = cond_var
        self.block = block

    def generate(self, context):
        out_s = context.next_state
        n_s = context.new_state()

        context.N(
            Mux(self.cond_var.generate(context),
                StateVariable(n_s),
                StateVariable(out_s))
        )

        context.push_state(n_s, out_s)
        self.block.generate(context)
        context.pop_state()

