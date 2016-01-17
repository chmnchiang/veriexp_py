from .statement import Statement
from verilog.variable import Mux, StateVariable
from verilog.module import Module

class FunctionDeclaration(Statement):
    def __init__(self, name, typ, args, block):
        self.name = name
        self.typ = typ
        self.args = args
        self.block = block

    def generate(self, context):
        context.module = Module(self.name)

        s = context.add_var('state', 32)
        context.state_var = s
        context.idle_state = context.new_state()
        context.start_state = context.new_state()

        context.add_input('clk', 1)
        start_var = context.add_input('start', 1)
        context.set_next_state(context.idle_state,
            Mux(start_var, 
                StateVariable(context.start_state), 
                StateVariable(context.idle_state)))
        for a in self.args:
            a.generate(context)

        context.result_var = context.add_output(
            'result', self.typ.length())
        context.add_output('done', 1)

        in_s = context.new_state()
        out_s = context.idle_state
        context.push_state(in_s, out_s)
        context.set_next_state(context.start_state, in_s)

        self.block.generate(context)

