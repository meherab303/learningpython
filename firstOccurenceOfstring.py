def firstOccurence(haystack,needle):
    
    # try:
    #     index=haystack.index(needle)
    #     return index
    # except ValueError:
    #     return -1

    # i=0
    # for j in range(0,len(haystack),1):
    #     if haystack[j]==needle[i]:
    #         i+=1
    #         if len(needle)==i:
    #             return j+1-len(needle)
               

                
    #     else:
    #         i=0 
                 
    # if i==0:
    #     return -1        
    
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:(i+len(needle))]==needle:
            return i+len(needle)-1
               

                
        
                 
    else:
        return -1           
    
print(firstOccurence("sadbutsad","sad"))       
