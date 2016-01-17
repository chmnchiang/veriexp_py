from .statement import Statement

class FuncArgDeclaration(Statement):
    def __init__(self, typ, name):
        self.typ = typ
        self.name = name

    def generate(self, context):
        context.add_input(self.name.name, self.typ.length(), True)
