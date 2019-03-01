class Lexer (object):
    def __init__(self,source_code):
        self.source_code = source_code

    def tokenize(self):
        # Stores tokens in a list
        tokens = []
        # Creates a word list of source code
        source_code = self.source_code.split()
        # Keeps track of the word index while lexing the source code
        source_index = 0
        # Keeps track of whether the program is lexing words or letters
        lexstate = 0
        # Loops through each word in source code to generate tokens
        while source_index < len(source_code):
            if lexstate == 0:
                print(source_code[source_index])
                # Lexstate is 1 after command is finished
                if source_code[source_index] == 'to':
                    lexstate = 1
            elif lexstate == 1:
                # Add equation to a list and print
                aftersource_code = list(source_code[source_index])
                print(aftersource_code)
            # Increments the source index
            source_index += 1
        return tokens
