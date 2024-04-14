from colorama import Fore

def raise_error(msg:str, token:dict=None):
    print(Fore.RED, end="")
    print(f"⚠️ 🥖 ERROR : {msg}")
    if token:
        print(f"Token ({token['type']}) \"{token['value']}\" at position {token['position']}")
    print(Fore.RESET, end="")
    exit(1)

def parse(tokens:list):
    # NON IMPLEMENTE !!!
    while tokens != []:
        tokens.pop(0)
    return True