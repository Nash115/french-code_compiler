from colorama import Fore
from frontend.ast_nodes import Stmt, Program, Exprs, BinaryExpr, Identifier, NumericLiteral
from frontend.scanner import scan_file, TokenType, Token

def raise_error(msg:str, token:Token=None):
    print(Fore.RED, end="")
    print(f"⚠️ 🥖 ERROR : {msg}")
    if token:
        print(f"Token ({token.type}) \"{token.value}\" at position {token.position}")
    print(Fore.RESET, end="")
    exit(1)

class Parser:
    def __init__(self, tokens: list = []):
        self.tokens = tokens

    def notEOF(self):
        return self.tokens[0].type != "EOF"

    def at(self):
        return self.tokens[0]
    
    def eat(self):
        prev = self.tokens.pop(0)
        return prev
    
    def expect(self, type: TokenType, err: str, token:Token=None):
        prev = self.eat()
        if not(prev.type) or prev.type != type:
            raise_error(err, prev, token)
        return prev

    def produceTokens(self, source_code : str) -> list:
        self.tokens = scan_file(source_code)

    def produceAST(self, source_code : str) -> Program:
        self.produceTokens(source_code)
        program = Program([])

        while self.notEOF():
            program.body.append(self.parseStmt())

        return program
    
    def parseStmt(self) -> Stmt:
        return self.parseExpr()
    
    def parseExpr(self) -> Exprs:
        return self.parseAdditiveExpr()

    def parseAdditiveExpr(self) -> Exprs:
        left = self.parseMultiplicativeExpr()
        while (self.at().value == "+" or self.at().value == "-"):
            operator = self.eat().value
            right = self.parseMultiplicativeExpr()
            left = BinaryExpr(left, right, operator)

        return left
    
    def parseMultiplicativeExpr(self) -> Exprs:
        left = self.parsePrimaryExpr()
        while (self.at().value == "*" or self.at().value == "/" or self.at().value == "%"):
            operator = self.eat().value
            right = self.parsePrimaryExpr()
            left = BinaryExpr(left, right, operator)

        return left

    def parsePrimaryExpr(self) -> Exprs:
        token = self.at().type

        if token == TokenType.Identifier:
            return Identifier(self.eat().value)

        elif token == TokenType.Number:
            return NumericLiteral(float(self.eat().value))

        elif token == TokenType.ParenthesisOpen:
            self.eat()
            value = self.parseExpr()
            self.expect(TokenType.ParenthesisClose, "Unexpected token found inside parenthesised expression. Expected closing parenthesis.")
            return value

        else:
            raise_error("Unexpected token found during parsing!", self.at())