def commonPrefix(listOfString):
    str1=listOfString[0]
    str2=listOfString[1]
    i=0
    prefix=''
    for j in range(0,len(str2),1):
        if str1[i]!=str2[j]:
            return prefix
            
         
        prefix+=str1[i]    
        i+=1  
            
    return prefix    
        
        
print(commonPrefix(["balower","ccvbabdakloao"]))

# def commonPrefix(s1,s2):
#     prefix=''
#     for i in range(min(len(s1),len(s2))):
#         if s1[i]!=s2[i]:
#             break 
#         prefix+=s1[i]
#     return prefix    
               
# print(commonPrefix("balower","bababdakloao"))
        
