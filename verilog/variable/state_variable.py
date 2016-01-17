from .variable import Variable

class StateVariable(Variable):
    def __init__(self, state):
        self.state = state

    def code_gen(self, context):
        yield str(context.get_statenum(self.state))
