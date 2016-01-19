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
        yield ');\n'
        for v in self.vars:
            yield from v.generate_declaration(context)


        # always block
        yield 'always @(posedge clk) begin\n'
        yield 'if (reset) state <= 0; else begin\n'
        yield 'case(state)\n'
        for st, ls in self.state_desc.items():
            if context.get_statenum(st) != st:
                continue
            yield '{}: begin\n'.format(st)
            for statement in ls:
                yield from statement.code_gen(context)
            yield 'end\n'
        yield 'endcase\n'
        yield 'end\nend\n'
        yield 'endmodule\n'
