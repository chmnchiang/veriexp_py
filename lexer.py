import ply.lex as lex

tokens = (
    'RETURN',
    'IDENT',
    'DIGITS'
)

literals = ['+', '-', '*', '/', '(', ')', '{', '}', ';', ',']

t_ignore  = ' \t'

def t_RETURN(t):
    r'return'
    return t

def t_IDENT(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t

def t_DIGITS(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()

if __name__ == '__main__':

    with open('test.ver') as f:
        lex.input(f.read())

        while True:
            tok = lex.token()
            if not tok:
                break
            print(tok.type, tok.value)
