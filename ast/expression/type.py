from .expression import Expression

class Type(Expression):
    def __init__(self, name):
        self.name = name

    def length(self):
        if self.name == 'int':
            return 32

        raise NotImplementedError
