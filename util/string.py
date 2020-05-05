def swapChars(string, pos1, pos2) :
    result = ""
    print(string)

    for i in range(0, len(string) - 1) :
        if i == pos1 :
            toAdd = string[pos2]
        elif i == pos2 :
            toAdd = string[pos1]
        else :
            toAdd = string[i]
        result = result + toAdd

    return result