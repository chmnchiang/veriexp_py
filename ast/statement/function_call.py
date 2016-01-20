from .statement import Statement
from verilog.variable import StateVariable, ConstValue, Mux
from verilog.statement import StoreReg

class FunctionCall(Statement):
    def __init__(self, func_name, args):
        self.func_name = func_name
        self.args = args

    def generate(self, context):
        self.args_var = [(str(a[0]), a[1].generate(context)) for a in self.args]

        clk, reset, start, result, done = (
            context.ident_map['clk'],
            context.ident_map['reset'],
            context.create_temp_var(1),
            context.create_temp_wire(32),
            context.create_temp_wire(1)
        )

        res_var = context.create_temp_var(32)

        bundle = {
            'clk': clk,
            'reset': reset,
            'start': start,
            'result': result,
            'done': done,
            **dict(self.args_var)
        }

        context.add_submodule(str(self.func_name), bundle)
        call_begin, call_init, call_waiting, call_end = [
            context.new_state() for i in range(4)
        ]
        # Call begin
        context.add_statement(call_begin,
            StoreReg(start, ConstValue(1))
        )
        context.set_next_state(call_begin, StateVariable(call_init))

        # Call init
        context.add_statement(call_init,
            StoreReg(start, ConstValue(0))
        )
        context.set_next_state(call_init, StateVariable(call_waiting))

        # Call wait
        context.set_next_state(
            call_waiting,
            Mux(
                done,
                StateVariable(call_end),
                StateVariable(call_waiting)
            )
        )

        # Call end
        context.add_statement(
            call_end,
            StoreReg(res_var, result)
        )
        
        context.join_state(context.cur_state, call_begin)
        context.insert_state()
        context.set_next_state(call_end, StateVariable(context.cur_state))

        return res_var
