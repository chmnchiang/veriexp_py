from .node import Node
from .variable import IOType
from .named import Named

class Module(Node, Named):
    def __init__(self, name):
        self.name = name
        self.vars = []
        self.state_desc = {}

    def code_gen(self, context):
        yield 'module {}'.format(self.name)
        yield '('
        fs = True
        for v in self.vars:
            if v.io_type == IOType.normal:
                continue
            if fs:
                fs = False
            else:
                yield ', '
            yield from v.code_gen(context)
        yield ')\n'
        for v in self.vars:
            yield from v.generate_declaration(context)


        # always block
        yield 'always @(posedge clk) begin\n'
        yield 'case('
        yield from context.state_var.code_gen(context)
        yield ')\n'
        for st, ls in self.state_desc.items():
            yield '{}: begin\n'.format(st)
            for statement in ls:
                yield from statement.code_gen(context)
            yield 'end\n'
        yield 'endcase\n'
        yield 'end\n'
        yield 'endmodule\n'
