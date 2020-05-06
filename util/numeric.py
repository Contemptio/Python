from util.general import error

def toFloat(string):
    try: 
        return float(string)
    except ValueError:
        error("Expected integer string, found: " + string + ".")

def toInteger(string):
    try: 
        return int(string)
    except ValueError:
        error("Expected integer string, found: " + string + ".")