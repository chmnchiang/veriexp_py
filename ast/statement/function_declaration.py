from .statement import Statement
from verilog.statement import StoreReg
from verilog.variable import Mux, StateVariable, ConstValue
from verilog.module import Module

class FunctionDeclaration(Statement):
    def __init__(self, name, typ, args, block):
        self.name = name
        self.typ = typ
        self.args = args
        self.block = block

    def generate(self, context):
        context.module = Module(self.name)

        context.add_var('state', 32)
        context.idle_state = context.new_state()
        context.start_state = context.new_state()

        context.add_input('clk', 1)
        context.add_input('reset', 1)
        start_var = context.add_input('start', 1)
        context.set_next_state(context.idle_state,
            Mux(start_var, 
                StateVariable(context.start_state), 
                StateVariable(context.idle_state)))
        for a in self.args:
            a.generate(context)

        context.add_output('result', self.typ.length())
        context.add_output('done', 1)

        in_s = context.new_state()
        out_s = context.idle_state
        context.push_state(in_s, out_s)
        context.set_next_state(context.start_state, in_s)
        context.add_statement(context.start_state, 
                StoreReg(context.ident_map['done'], ConstValue(0)))

        self.block.generate(context)

