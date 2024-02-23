def incoding(N) :
    key = 1004
    code = N ^ key

    return code

def decoding(N) :
    key = 1004
    code = N ^ key

    return code


E = 1000
print(incoding(E))

D = 4
print(decoding(D))