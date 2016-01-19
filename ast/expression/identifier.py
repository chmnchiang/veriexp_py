from .expression import Expression

class Identifier(Expression):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def generate(self, context):
        return context.ident_map[self.name]
