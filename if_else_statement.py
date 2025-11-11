import re

# Definisaun token sira
token_specification = [
    ('if', r'if'),
    ('else', r'else'),
    ('lparen', r'\('),
    ('rparen', r'\)'),
    ('lbrace', r'\{'),
    ('rbrace', r'\}'),
    ('eq', r'>|<|==|!=|>=|<='),
    ('assign', r'='),
    ('number', r'\d+'),
    ('identifier', r'[a-zA-Z_]\w*'),
    ('semicolon', r';'),
    ('skip', r'[ \t\n]+'),
    ('mismatch', r'.'),
]

# Kompila regex
tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

# Input string
code = 'if (x > 5) {y = 1;} else {y = 0;}'

# Tokenize
tokens = []
for mo in re.finditer(tok_regex, code):
    kind = mo.lastgroup
    value = mo.group()
    if kind == 'skip':
        continue
    elif kind == 'mismatch':
        raise RuntimeError(f'Unexpected token: {value}')
    tokens.append((kind, value))

# Hatudu rezultadu
for token in tokens:
    print(token)
