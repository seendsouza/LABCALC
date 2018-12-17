import lexer
def main():
    """
    Read the LABCALC source code and store it in a variable
    """
    content = ""
    with open('./test.lang','r') as file:
    #
    # Lexer
    #
        while True:
            line = file.readline()
            # Call and initialize lexer class
            linestring = ''.join(map(str, line))
            lex = lexer.Lexer(linestring)
            # Call tokenize method
            tokens = lex.tokenize()
            if not line:
                break

main()
