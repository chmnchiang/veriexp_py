from .statement import Statement
from verilog.variable import StateVariable, ConstValue
from verilog.statement import StoreReg

class AsyncFunctionCall(Statement):
    def __init__(self, func_name, args, return_type,
                 done_var_name, res_var_name):
        self.func_name = func_name
        self.args = args
        self.return_type = return_type
        self.done_var_name = done_var_name
        self.res_var_name = res_var_name

    def generate(self, context):
        self.args_var = [(str(a[0]), a[1].generate(context)) for a in self.args]
        ret_len = self.return_type.length()

        clk, reset, start = (
            context.ident_map['clk'],
            context.ident_map['reset'],
            context.create_temp_var(1),
        )

        done_var = context.add_wire(
            self.done_var_name.name, 1
        )
        result_var = context.add_wire(
            self.res_var_name.name, ret_len
        )

        bundle = {
            'clk': clk,
            'reset': reset,
            'start': start,
            'result': result_var,
            'done': done_var,
            **dict(self.args_var)
        }

        context.add_submodule(str(self.func_name), bundle)
        call_begin, call_init = (context.cur_state, context.new_state())

        # Call begin
        context.add_statement(call_begin,
            StoreReg(start, ConstValue(1))
        )
        context.set_next_state(call_begin, StateVariable(call_init))

        # Call init
        context.add_statement(call_init,
            StoreReg(start, ConstValue(0))
        )
        context.set_next_state(call_init, 
                               StateVariable(context.next_state))

