import sys

class NotYetImplemented(Exception) :
    pass

def error(message) :
    print(message)
    sys.exit(1) 