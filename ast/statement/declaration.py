from .statement import Statement

class Declaration(Statement):
    def __init__(self, typ, name):
        self.typ = typ
        self.name = name

    def generate(self, context):
        context.add_var(self.name.name, self.typ.length())
        context.join_state(context.cur_state, context.next_state)
