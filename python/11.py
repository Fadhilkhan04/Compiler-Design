
import re

def tokenize(expr):
    token_pattern = r'\d+|[-+*/()]'

    return re.findall(token_pattern, expr)

def parse_expr(tokens):
    def parse_factor():
        if tokens[0] == '(':
            tokens.pop(0)  # Remove '('
            node = parse_expr(tokens)
            tokens.pop(0)  # Remove ')'
            return node
        return {'type': 'number', 'value': tokens.pop(0)}

    def parse_binop(subparser, ops):
        node = subparser()
        while tokens and tokens[0] in ops:
            op = tokens.pop(0)
            right = subparser()
            node = {'type': 'binop', 'op': op, 'left': node, 'right': right}
        return node

    return parse_binop(lambda: parse_binop(parse_factor, ('*', '/')), ('+', '-'))


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
