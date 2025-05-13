
import re

def tokenize(expr):
    token_pattern = r'\d+|[-+*/()]'

    return re.findall(token_pattern, expr)

def parse_expr(tokens):
    def parse_factor():
        token = tokens.pop(0)
        if token == '(':
            node = parse_expr(tokens)  # Pass tokens here
            tokens.pop(0)  # remove ')'
            return node
        else:
            return {'type': 'number', 'value': token}

    def parse_term():
        node = parse_factor()
        while tokens and tokens[0] in ('*', '/'):
            op = tokens.pop(0)
            right = parse_factor()
            node = {'type': 'binop', 'op': op, 'left': node, 'right': right}
        return node

    node = parse_term()
    while tokens and tokens[0] in ('+', '-'):
        op = tokens.pop(0)
        right = parse_term()
        node = {'type': 'binop', 'op': op, 'left': node, 'right': right}
    return node

def print_ast(node, indent=0):
    space = '  ' * indent
    if node['type'] == 'number':
        print(space + "Number:", node['value'])
    elif node['type'] == 'binop':
        print(space + "Operator:", node['op'])
        print(space + "Left:")
        print_ast(node['left'], indent + 1)
        print(space + "Right:")
        print_ast(node['right'], indent + 1)

# Example usage
expr = "3 + 4 * (5 - 4)"
tokens = tokenize(expr)
ast = parse_expr(tokens)
print("Abstract Syntax Tree:")
print_ast(ast)
