def countOfPrefix(words,s):
    c=0
    for elem in words:
        if s[0:len(elem)]==elem:
            c+=1
    return c        
print(countOfPrefix(["a","b","c","ab","bc","abc"], "abc"))