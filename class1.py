# Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
class Query():
    def __init__(self):
        self.word = ""
    def getstring(self):
        self.word = input("Enter a word: ")
    def printstring(self):
        print(self.word.upper())
ok = Query()        
ok.getstring()
ok.printstring()                            