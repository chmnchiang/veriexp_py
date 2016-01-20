from .node import Node

class Submodule(Node):

    def __init__(self, mod_name, args):
        self.mod_name = mod_name
        self.args = args

    def code_gen(self, context):
        name = context.get_temp_var_name()

        yield '{} {}(\n'.format(self.mod_name, name)
        first = True
        for n, v in self.args.items():
            if first:
                first = False
            else:
                yield ',\n'

            yield '.{}('.format(n)
            yield from v.code_gen(context)
            yield ')'
        yield '\n);\n'

