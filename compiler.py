import frontend.scanner as scanner
import frontend.parser as parser

if __name__ == "__main__":
    code_file = scanner.sys.argv[1] # For example: "test.baguette"

    parser = parser.Parser()
    parser.produceTokens(code_file)
    # print(parser.tokens)
    program = parser.produceAST(code_file)

    print(program)