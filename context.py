from verilog.variable import (Variable, 
                              WireVariable,
                              IOType, 
                              RegVariable, 
                              StateVariable)
from verilog.statement import Statement, StoreReg
from verilog.submodule import Submodule

class Context:
    def __init__(self):
        self.module = None
        self.ident_map = {}
        self.states = []
        self.idle_state = None
        self.start_state = None
        self.temp_var_cnt = 0

        self.special_var = {}

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

    def add_wire(self, name, length):
        var = WireVariable(name=name, length=length, io_type=IOType.normal)
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
            StoreReg(self.ident_map['state'], next_state)
        )

    def add_submodule(self, name, bundle):
        self.module.submodules.append(Submodule(name, bundle))

    def A(self, statement):
        self.add_statement(self.cur_state, statement)

    def N(self, next_state):
        self.set_next_state(self.cur_state, next_state)

    def get_temp_var_name(self):
        s = "_T%d" % self.temp_var_cnt
        self.temp_var_cnt += 1
        return s

    def create_temp_var(self, length):
        name = self.get_temp_var_name()
        return self.add_var(name, length)

    def create_temp_wire(self, length):
        name = self.get_temp_var_name()
        return self.add_wire(name, length)

    @property
    def cur_state(self):
        return self.stack[-1][0]

    @property
    def next_state(self):
        return self.stack[-1][1]

    def push_state(self, p, f):
        self.stack.append((p, f))

    def pop_state(self):
        return self.stack.pop()

    def insert_state(self):
        o_s = self.cur_state
        self.stack[-1] = (self.new_state(), self.stack[-1][1])
        return o_s




