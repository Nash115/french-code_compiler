import sys

keywords = {
    ";": "end_of_instruction",
    "=": "assignation",
    "(": "parenthesis_open",
    ")": "parenthesis_close",

    "vrai": "bool",
    "faux": "bool",

    "afficher": "print",
}

def is_a_known_keyword(line:str, index:int) -> bool:
    if line[index] in [' ', '\n', '\t']:
        return True
    for keyword in keywords:
        if line[index:index+len(keyword)] == keyword:
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
                tokens.append({'type': "number",'value': int(number), 'position': (line_index, index)})
                continue

            # string
            if line[index] == '"':
                string = ""
                index += 1
                while index < len(line) and line[index] != '"':
                    string += line[index]
                    index += 1
                tokens.append({'type': "string",'value': string, 'position': (line_index, index)})
                index += 1
                continue

            keyword_found = False
            for keyword, keyword_type in keywords.items():
                if line[index:index+len(keyword)] == keyword:
                    tokens.append({'type': keyword_type,'value': line[index:index+len(keyword)],'position': (line_index, index)})
                    index += len(keyword)
                    keyword_found = True
                    break
            if not(keyword_found):
                identifiant = ""
                while not(is_a_known_keyword(line, index)) and index < len(line):
                    identifiant += line[index]
                    index += 1
                tokens.append({'type': "ident",'value': identifiant, 'position': (line_index, index)})
    return tokens

if __name__ == "__main__":
    tokens = scan_file(sys.argv[1])
    print(tokens)