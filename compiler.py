import tools.scanner as scanner
import tools.parser as parser

if __name__ == "__main__":
    tokens = scanner.scan_file(scanner.sys.argv[1])
    parser.parse(list(tokens))
    print(tokens)