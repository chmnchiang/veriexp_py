from .temp_variable import TempVariable

class Mux(TempVariable):

    def __init__(self, cond_var, if_var, else_var):
        self.cond_var = cond_var
        self.if_var = if_var
        self.else_var = else_var

    def code_gen(self, context):
        yield '('
        yield from self.cond_var.code_gen(context)
        yield ') ? ('
        yield from self.if_var.code_gen(context)
        yield ') : ('
        yield from self.else_var.code_gen(context)
        yield ')'
