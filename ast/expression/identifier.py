from .expression import Expression

class Identifier(Expression):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
