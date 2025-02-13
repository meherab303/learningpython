def prefixOfArray(s,words):
    string=''
    for elem in words:
        string+=elem 
        if string==s:
            return True
        if len(string) >len(s):
            return False
    return False     
print(prefixOfArray("aaa",["aa","aaa","fjaklfj"]))        