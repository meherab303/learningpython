def countVowel(words,left,right):
    
    count=0
    for i in range(left,right+1,1):
         if words[i].lower().startswith(('a', 'e', 'i', 'o', 'u')) and words[i].lower().endswith(('a', 'e', 'i', 'o', 'u')):
                count+=1 
           
    return count    

print(countVowel(["hey","aeo","mu","ooo","artro"],1,4))