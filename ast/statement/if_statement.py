from .statement import Statement
from verilog.variable import Mux, StateVariable

class IfStatement(Statement):
    def __init__(self, cond_var, if_block, else_block=None):
        self.cond_var = cond_var
        self.if_block = if_block
        self.else_block = else_block

    def generate(self, context):
        out_s = context.next_state
        if_s = context.new_state()
        else_s = (context.new_state() 
                  if self.else_block is not None else out_s)

        context.N(
            Mux(self.cond_var.generate(context),
                StateVariable(if_s),
                StateVariable(else_s))
        )

        context.push_state(if_s, out_s)
        self.if_block.generate(context)
        context.pop_state()

        if self.else_block is not None:
            context.push_state(else_s, out_s)
            self.else_block.generate(context)
            context.pop_state()

