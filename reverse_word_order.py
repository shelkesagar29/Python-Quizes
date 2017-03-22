def revword(inp):
    req=inp.split()
    req.reverse()
    #insted of using in built reverse() we could write something like
    #req=[x for x in req[::-1]] This way we are reversing lsit
    #return (' '.join(req))
    return(' '.join(req))

string=input("Enter string to reverse\n")
pr=revword(string)
print(pr)