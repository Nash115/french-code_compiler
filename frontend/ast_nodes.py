###################################
############### AST ###############
###################################

class NodeType:
    Program = "Program"
    NumericLiteral = "NumericLiteral"
    Identifier = "Identifier"
    BinaryExpr = "BinaryExpr"

class Stmt:
    def __init__(self, kind: NodeType):
        self.kind = kind
    def __repr__(self):
        return f"Stmt(kind: {self.kind})"

class Program(Stmt):
    def __init__(self, body: list[Stmt]):
        super().__init__(NodeType.Program)
        self.body = body
    def __repr__(self):
        s = f"Program(kind: {self.kind}, body: [\n"
        for b in self.body:
            s += f"\t{b}, \n"
        s = s[:-3] + "\n"
        s += "])"
        return s

class Exprs(Stmt):
    def __init__(self, kind: NodeType):
        super().__init__(kind)
    def __repr__(self):
        return f"Exprs(kind: {self.kind})"

class BinaryExpr(Exprs):
    def __init__(self, left: Exprs, right: Exprs, operator: str):
        super().__init__(NodeType.BinaryExpr)
        self.left = left
        self.right = right
        self.operator = operator
    def __repr__(self):
        return f"BinaryExpr(kind: {self.kind}, left: {self.left}, right: {self.right}, operator: {self.operator})"

class Identifier(Exprs):
    def __init__(self, symbol: str):
        super().__init__(NodeType.Identifier)
        self.symbol = symbol
    def __repr__(self):
        return f"Identifier(kind: {self.kind}, symbol: {self.symbol})"

class NumericLiteral(Exprs):
    def __init__(self, value: float):
        super().__init__(NodeType.NumericLiteral)
        self.value = value
    def __repr__(self):
        return f"NumericLiteral(kind: {self.kind}, value: {self.value})"