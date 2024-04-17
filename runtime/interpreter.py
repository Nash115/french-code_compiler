from runtime.values import ValueType, RuntimeVal, NumberVal, NullVal
from frontend.ast_nodes import NodeType, Stmt, NumericLiteral, BinaryExpr, Program
from colorama import Fore

def raise_error(msg:str, ast_node:Stmt=None):
    print(Fore.RED, end="")
    print(f"⚠️ 🥖 Interpreter ERROR : {msg}")
    if ast_node:
        print(ast_node)
    print(Fore.RESET, end="")
    exit(1)

def eval_program(program:Program) -> RuntimeVal:
    lastEvaluated = NullVal()
    for statement in program.body:
        lastEvaluated = evaluate(statement)
    return lastEvaluated

def eval_numeric_binary_expression(left:NumberVal, right:NumberVal, operator:str) -> NumberVal:
    if operator == "+":
        return NumberVal(left.value + right.value)
    elif operator == "-":
        return NumberVal(left.value - right.value)
    elif operator == "*":
        return NumberVal(left.value * right.value)
    elif operator == "/":
        if right.value == 0:
            raise_error(f"Tried to divide by zero")
        return NumberVal(left.value / right.value)
    elif operator == "%":
        if right.value == 0:
            raise_error(f"Tried to divide by zero")
        return NumberVal(left.value % right.value)
    else:
        raise_error(f"Unknown operator {operator}")

def eval_binary_expression(binop:BinaryExpr) -> RuntimeVal:
    leftHandSide = evaluate(binop.left)
    rightHandSide = evaluate(binop.right)

    if leftHandSide.type == ValueType.number and rightHandSide.type == ValueType.number:
        return eval_numeric_binary_expression(leftHandSide, rightHandSide, binop.operator)
    
    return NullVal()

def evaluate(astNode:Stmt) -> RuntimeVal:
    if astNode.kind == NodeType.NumericLiteral:
        return NumberVal(astNode.value)
    
    if astNode.kind == NodeType.NullLiteral:
        return NullVal()

    if astNode.kind == NodeType.BinaryExpr:
        return eval_binary_expression(astNode)

    if astNode.kind == NodeType.Program:
        return eval_program(astNode)

    else:
        raise_error(f"Unknown AST Node",astNode)
        return NullVal()