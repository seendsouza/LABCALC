class Lexer (object):
    def __init__(self,source_code):
        self.source_code = source_code
    def tokenize(self):
        # Tokens are stored here
        tokens = []
        # Create word list of source code
        source_code = self.source_code.split()
        # Keeps track of word index we're at in source code
        source_index = 0
        # Keeps track of whether we're lexing words or letters
        lexstate = 0
        # Loops through each word in source code to generate tokens
        while source_index < len(source_code):
            if lexstate == 0:
                print(source_code[source_index])
                # Lexstate is 1 after command is finished
                if source_code[source_index] == 'to':
                    lexstate = 1
            else:
                # Add equation to a list and print
                aftersource_code = source_code[source_index]
                listasc = list(aftersource_code)
                print(listasc)
            # Adds 1 to the source index
            source_index += 1
        return tokens
