from .statement import Statement
from verilog.variable import Mux, StateVariable

class WhileStatement(Statement):
    def __init__(self, cond_var, block):
        self.cond_var = cond_var
        self.block = block

    def generate(self, context):
        in_s = context.cur_state
        out_s = context.next_state
        n_s = context.new_state()

        context.N(
            Mux(self.cond_var.generate(context),
                StateVariable(n_s),
                StateVariable(out_s))
        )

        context.push_state(n_s, in_s)
        self.block.generate(context)
        context.pop_state()

