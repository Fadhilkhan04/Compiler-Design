class Node:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class CodeGen:
    def __init__(self):
        self.reg = 0
        self.code = []
        self.ops = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV'}

    def new_reg(self):
        self.reg += 1
        return f"R{self.reg}"

    def gen(self, node):
        if not node.left and not node.right:
            r = self.new_reg()
            self.code.append(f"LOAD {r}, {node.val}")
            return r
        if node.val == '=':
            r = self.gen(node.right)
            self.code.append(f"STORE {node.left.val}, {r}")
            return
        l = self.gen(node.left)
        r = self.gen(node.right)
        self.code.append(f"{self.ops[node.val]} {l}, {r}")
        return l

    def print(self):
        print("Assembly Code:\n" + '\n'.join(self.code))

# Example: a = 3 * (5 + 3)
ast = Node('=', Node('a'), Node('*', Node('3'), Node('+', Node('5'), Node('3'))))

cg = CodeGen()
cg.gen(ast)
cg.print()
