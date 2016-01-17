from .statement import Statement

class Block(Statement):

    def __init__(self, statements):
        self.statements = statements

    def generate(self, context):
        in_s = context.cur_state

        for stmt in self.statements:
            out_s = context.new_state()
            context.push_state(in_s, out_s)
            stmt.generate(context)
            context.pop_state(in_s, out_s)

            in_s = out_s

        context.join_state(in_s, context.next_state) 


