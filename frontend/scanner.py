import sys

keywords = {
    "assignation": ["="],
    "parenthesis_open": ["("],
    "parenthesis_close": [")"],
    "binary_operator": ["+", "-", "*", "/", "%"],

    "bool": ["vrai", "faux"],
    "end_of_instruction": [";"],
    "print": ["afficher"],

    "EOF": []
}

class TokenType:
    Identifier = "ident"
    Number = "number"
    String = "string"
    Assignation = "assignation"
    ParenthesisOpen = "parenthesis_open"
    ParenthesisClose = "parenthesis_close"
    BinaryOperator = "binary_operator"

    Bool = "bool"
    EndOfInstruction = "end_of_instruction"
    Print = "print"

class Token:
    def __init__(self, type:str, value, position:tuple) -> None:
        self.type = type
        self.value = value
        self.position = position
    def __repr__(self) -> str:
        return f"Token({self.type}, {self.value}, {self.position})"

def is_a_known_keyword(line:str, index:int) -> bool:
    if index >= len(line):
        return True
    if line[index] in [' ', '\n', '\t']:
        return True
    for keyword,symbols in keywords.items():
        for symbol in symbols:
            if line[index:index+len(symbol)] == symbol:
                return True
    return False

def scan_file(file_name:str)->list:
    tokens = []
    with open(file_name, 'r') as f:
        file = f.readlines()
    for line_index,line in enumerate(file):
        index = 0
        while index < len(line):
             # ignore spaces
            if line[index] in [' ', '\n', '\t']:
                index += 1
                continue

            # number
            if line[index] in "0123456789":
                number = ""
                while index < len(line) and line[index] in "0123456789":
                    number += line[index]
                    index += 1
                tokens.append(Token(type="number", value=int(number), position=(line_index, index)))
                continue

            # string ###
            if line[index] == '"':
                string = ""
                index += 1
                while index < len(line) and line[index] != '"':
                    string += line[index]
                    index += 1
                tokens.append(Token(type="string", value=string, position=(line_index, index)))
                index += 1
                continue

            keyword_found = False
            for keyword_type, symbols in keywords.items():
                for symbol in symbols:
                    if line[index:index+len(symbol)] == symbol:
                        tokens.append(Token(type=keyword_type, value=line[index:index+len(symbol)], position=(line_index, index)))
                        index += len(symbol)
                        keyword_found = True
                        break
            if not(keyword_found):
                identifiant = ""
                while not(is_a_known_keyword(line, index)) and index < len(line):
                    identifiant += line[index]
                    index += 1
                tokens.append(Token(type="ident", value=identifiant, position=(line_index, index)))
    tokens.append(Token(type="EOF", value="EOF", position=(line_index, index)))
    return tokens

if __name__ == "__main__":
    tokens = scan_file(sys.argv[1])
    print(tokens)