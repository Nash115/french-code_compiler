import frontend.scanner as scanner
import frontend.parser as parser
import runtime.interpreter as interpreter

if __name__ == "__main__":
    code_file = scanner.sys.argv[1] # For example: "test.baguette"

    parser = parser.Parser()
    program = parser.produceAST(code_file) # This is the AST
    result = interpreter.evaluate(program)
    print(f"Valeur du dernier résultat : {result.value}")