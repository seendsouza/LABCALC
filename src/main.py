import lexer
def main():
# Read the LABCALC source code and store it in a variable
    content = ""
    with open('src/test.lang','r') as file:
    #
    # Lexer
    #
    while readlineTrue:
        line = file.readline()
        # Call and initialize lexer class
        linestring = ''.join(map(str, line))
        lex = lexer.Lexer(linestring)
        # Call tokenize method
        tokens = lex.tokenize()
        if not line:
            break

main()
