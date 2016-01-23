from .expression import Expression

class Type(Expression):
    def __init__(self, length):
        self._length = length

    def length(self):
        return self._length

        # raise NotImplementedError
