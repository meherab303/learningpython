def pairOfsString(words):
    pairs=0
    for i in range(len(words)):
        setss=set(words[i])
        for j in range(i+1,len(words),1):
            if setss==set(words[j]):
                pairs+=1
    return pairs 
print(pairOfsString(["aba","aabb","abcd","bac","aabc"]))           