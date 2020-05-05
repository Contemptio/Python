import sys

def error(message) :
    print(message)
    sys.exit(1)

def toInteger(string):
    try: 
        return int(string)
    except ValueError:
        error("Expected integer string, found: " + string + ".")