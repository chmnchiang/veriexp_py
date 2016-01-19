import lexer
import ply.yacc as yacc
from verilog.module import Module
from ast import *
from context import Context

tokens = lexer.tokens
start = 'program'

precedence = (
    ('left', '|'),
    ('left', '&'),
    ('left', '<', '>', 'EQUAL', 'NOTEQUAL'),
    ('left', 'LEFTSHIFT', 'RIGHTSHIFT'),
    ('left', '+', '-'),
    ('left', '*', '/'),
)

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
        p[1].append(p[2])
        p[0] = p[1]

def p_declaration(p):
    '''statement : type ident ';' '''
    p[0] = Declaration(typ=p[1], name=p[2])

def p_assignment(p):
    '''statement : ident '=' expression ';' '''
    p[0] = Assignment(p[1], p[3])

def p_if_statement(p):
    '''statement : IF '(' expression ')' block '''
    p[0] = IfStatement(p[3], p[5])

def p_while_statement(p):
    '''statement : WHILE '(' expression ')' block '''
    p[0] = WhileStatement(p[3], p[5])

def p_return_statement(p):
    '''statement : RETURN expression ';' '''
    p[0] = ReturnStatement(p[2])

def p_ident_expression(p):
    '''expression : ident '''
    p[0] = p[1]

def p_constant_expression(p):
    '''expression : constant '''
    p[0] = p[1]

def p_numerical_constant(p):
    '''constant : DIGITS '''
    p[0] = Constant(p[1])

def p_binary_expression(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
                  | expression '<' expression
                  | expression '>' expression
                  | expression '&' expression
                  | expression '|' expression
                  | expression EQUAL expression
                  | expression NOTEQUAL expression
                  | expression LEFTSHIFT expression
                  | expression RIGHTSHIFT expression
                  '''
    p[0] = BinaryOP(p[1], p[2], p[3])

def p_parenthesis_expression(p):
    '''expression : '(' expression ')' '''
                  
    p[0] = p[2]

def p_error(p):
    print('Error', p)

parser = yacc.yacc()

def parse_file(fn):
    with open(fn) as f:
        top = parser.parse(f.read())

    context = Context()
    top.generate(context)
    print(*(context.module.code_gen(context)), sep='')

if __name__ == '__main__':
    parse_file('f.ver')
