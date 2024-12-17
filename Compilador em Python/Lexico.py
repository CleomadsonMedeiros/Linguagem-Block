import ply.lex as lex     #importa módulo ply.lex e o renomeia para lex

# Tokens
tokens = ("PLUS", "MINUS", "TIMES", "DIVIDE", "LPAREN", "RPAREN", "NUMBER", "ID")
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ID = r'[A-Za-z_][A-Za-z0-9_]*'

#Ignore Token
t_ignore  = ' \t\n'

#Foo Tokens
t_foo_ignore = ' \t'
t_foo_NUMBER = r'\d+'

#Bar Tokens
t_bar_ignore = ' \t'
t_bar_NUMBER = r'\d+'

#States
states = (('foo', 'exclusive'), ('bar', 'inclusive'))

#Token Functions
def t_NUMBERFLOAT(t):
     r'\d+\.\d+'
     t.value = float(t.value)
     return t

def t_NUMBER(t):
     r'\d+'
     t.value = int(t.value)    
     return t

def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

def t_error(t):
     print("Caractere ilegal '%s'" % t.value[0])
     t.lexer.skip(1)


#Foo Functions
def foo_newline(t):
     r'\n'
     t.lexer.lineno += 1

def t_foo_newline(t):
  r'\n'
  t.lexer.lineno += 1

def t_foo_error(t):
  print('error in foo state, %s' % t.value[0])
  t.lexer.skip(1)

def t_begin_foo(t):
  r'<foo>'
  t.lexer.begin('foo')

def t_foo_end_foo(t):
  r'\</foo\>'
  t.lexer.begin('INITIAL')

#Bar Functions - O fato de bar ser inclusive, não é necessário fazer funções que já existem no estado INITIAL
def t_begin_bar(t):
  r'<bar>'
  t.lexer.begin('bar')

def t_bar_end_bar(t):
  r'\</bar\>'
  t.lexer.begin('INITIAL')

lexer = lex.lex()
lex.input("Fora do Foo <foo> 123 dentro do foo </foo> <bar> top 5 omaga dentro do bar </bar>")
for l in lexer:
  print(l.value)
