import lexer
import ply.yacc as yacc
from verilog.module import Module
from ast import *
from context import Context

tokens = lexer.tokens
start = 'program'


def p_program(p):
    '''program : func_decl'''
    p[0] = p[1]


def p_function_declaration(p):
    '''func_decl : type ident '(' func_args ')' block'''
    p[0] = FunctionDeclaration(p[2], p[1], p[4], p[6])


def p_type(p):
    '''type : IDENT'''
    p[0] = Type(p[1])


def p_ident(p):
    '''ident : IDENT'''
    p[0] = Identifier(p[1])

def p_func_args(p):
    '''func_args : 
                 | func_arg_decl
                 | func_args ',' func_arg_decl'''
    if len(p) == 1:
        p[0] = []
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_func_arg_decl(p):
    '''func_arg_decl : type ident'''
    p[0] = FuncArgDeclaration(p[1], p[2])

def p_block(p):
    '''block : '{' statements '}' '''
    p[0] = Block(p[2])

def p_statements(p):
    '''statements :
                  | statement
                  | statements statement '''
    if len(p) == 1:
        p[0] = []
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_return_statement(p):
    '''statement : RETURN ident ';' '''
    p[0] = ReturnStatement(p[2])

def p_return(t):
    '''return : RETURN'''

def p_error(p):
    print('Error', p)

if __name__ == '__main__':
    parser = yacc.yacc()
    # parser.parse('abc')
    with open('test.ver') as f:
        top = parser.parse(f.read())

    context = Context()
    top.generate(context)
    print(*(context.module.code_gen(context)), sep='')
    # print(''.join(context.module.code_gen(context)))
