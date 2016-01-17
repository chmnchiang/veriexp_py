from verilog.variable import (Variable, 
                              WireVariable,
                              IOType, 
                              RegVariable, 
                              StateVariable)
from verilog.statement import Statement, StoreReg

class Context:
    def __init__(self):
        self.module = None
        self.ident_map = {}
        self.states = []
        self.idle_state = None
        self.start_state = None
        self.state_var = None
        self.result_var = None

        self.stack = []

    def add_input(self, name, length, is_func_arg=False):
        var = WireVariable(name=name, length=length, io_type=IOType.input)
        self.module.vars.append(var)

        if is_func_arg:
            wire_var = var
            var = RegVariable(name='_'+name, length=length, io_type=IOType.normal)
            self.module.vars.append(var)
            self.add_initial_value(var, wire_var)

        self.regist_name(name, var)
        return var

    def add_output(self, name, length):
        var = RegVariable(name=name, length=length, io_type=IOType.output)
        self.module.vars.append(var)
        self.regist_name(name, var)
        return var

    def add_var(self, name, length):
        var = RegVariable(name=name, length=length, io_type=IOType.normal)
        self.module.vars.append(var)
        self.regist_name(name, var)
        return var

    def regist_name(self, name, var):
        self.ident_map[name] = var

    def new_state(self):
        t = len(self.states)
        self.states.append(t)
        self.module.state_desc[t] = []
        return t

    def get_statenum(self, state):
        if self.states[state] != state:
            self.states[state] = self.get_statenum(self.states[state])

        return self.states[state]

    def join_state(self, s1, s2):
        f1 = self.get_statenum(s1)
        f2 = self.get_statenum(s2)
        self.states[f1] = f2

    def add_statement(self, state, statement):
        assert isinstance(statement, Statement)
        
        self.module.state_desc[state].append(statement)

    def add_initial_value(self, lhs, rhs):
        assert self.start_state is not None
        self.add_statement(self.start_state,
            StoreReg(lhs, rhs))

    def set_next_state(self, state, next_state):
        if type(next_state) is int:
            next_state = StateVariable(next_state)
        assert isinstance(next_state, Variable)
        
        self.module.state_desc[state].append(
            StoreReg(self.state_var, next_state)
        )

    def A(self, statement):
        self.add_statement(self.cur_state, statement)

    def N(self, next_state):
        self.set_next_state(self.cur_state, next_state)

    @property
    def cur_state(self):
        return self.stack[-1][0]

    @property
    def next_state(self):
        return self.stack[-1][0]

    def push_state(self, p, f):
        self.stack.append((p, f))

    def pop_state(self, p, f):
        return self.stack.pop()




