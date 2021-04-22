import base64
def encrypter(s):
    return (base64.b64encode(s.encode()))


#The argument here should be in bytecode
def decrypter(es):
    return (base64.b64decode(es))

if __name__=="__main__":

    encrypter("Rishav")
    b="TGCJHGVkhv"
    test=b.encode()
    
    print(test)