# Tokenizer
def tokenize(expr):
    import re
    return re.findall(r'\d+|[-+*/()]', expr)

# AST Parser (Minimized)
def parse_expr(tokens):
    def parse_factor():
        if tokens[0] == '(':
            tokens.pop(0)
            node = parse_expr(tokens)
            tokens.pop(0)  # remove ')'
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

# AST Printer
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

# TAC Generator
class TACGenerator:
    def __init__(self):
        self.temp_count = 1
        self.code = []

    def get_temp(self):
        temp = f"t{self.temp_count}"
        self.temp_count += 1
        return temp

    def generate(self, node):
        if node['type'] == 'number':
            return node['value']
        left = self.generate(node['left'])
        right = self.generate(node['right'])
        temp = self.get_temp()
        self.code.append(f"{temp} = {left} {node['op']} {right}")
        return temp

# Example usage
expr = "3 + 4 * (2 - 1)"
tokens = tokenize(expr)
ast = parse_expr(tokens)

print("Abstract Syntax Tree:")
print_ast(ast)

print("\nThree-Address Code:")
generator = TACGenerator()
generator.generate(ast)
for line in generator.code:
    print(line)
