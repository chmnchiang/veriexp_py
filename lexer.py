import ply.lex as lex

reserved = (
    'RETURN',
    'IF',
    'ELSE',
    'WHILE',
    'INT',
    'LONG',
    'BOOL',
    'BITS',
    'ASYNC',
    'AWAIT',
)

tokens = reserved + (
    'IDENT',
    'DIGITS',
    'EQUAL',
    'NOTEQUAL',
    'GREATEREQUAL',
    'LESSEQUAL',
    'LEFTSHIFT',
    'RIGHTSHIFT',
    'MAPSTO',
    'PLUSEQUAL',
    'MINUSEQUAL',
    'LEFTSHIFTEQUAL',
    'RIGHTSHIFTEQUAL',
    'OPAND',
    'OPOR',
)

# literals = ['+', '-', '*', '/', '(', ')', '{', '}', ';', ',', '<', '>']
literals = '+-*/()[]{};,<>=&|!'

t_ignore  = ' \t'

t_EQUAL = '=='
t_NOTEQUAL = '!='
t_GREATEREQUAL = '>='
t_LESSEQUAL = '<='
t_LEFTSHIFT = '<<'
t_RIGHTSHIFT = '>>'
t_OPAND = '&&'
t_OPOR = '\|\|'
t_MAPSTO = '->'

t_PLUSEQUAL = '\+='
t_MINUSEQUAL = '-='
t_LEFTSHIFTEQUAL = '<<='
t_RIGHTSHIFTEQUAL = '>>='

reserved_map = {}
for r in reserved:
    reserved_map[r.lower()] = r

def t_IDENT(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved_map.get(t.value, 'IDENT')
    return t

def t_DIGITS(t):
    r'\d+'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()

if __name__ == '__main__':

    with open('f.ver') as f:
        lex.input(f.read())

        while True:
            tok = lex.token()
            if not tok:
                break
            print(tok.type, tok.value)
