# def commonPrefix(listOfString):
#     str1=listOfString[0]
#     str2=listOfString[1]
#     i=0
#     prefix=''
#     for j in range(0,len(str2),1):
#         if str1[i]!=str2[j]:
#             return prefix
            
         
#         prefix+=str1[i]    
#         i+=1  
#     # if(len(listOfString)>2):
#     #     for i in range(2,len(listOfString),1):

#     #         if not str(listOfString[i]).startswith(prefix):
                
            
#     #          return '' 
           
#     return prefix    
        
        
# print(commonPrefix(["flll","flll","fl"]))





# def commonPrefix(listOfString):
    
#     new_var_dic={}
#     for i in range(0,len(listOfString),1):
#         new_var_dic[f"var_{i}"]=listOfString[i]

#     minLength=len(listOfString[0])
#     for i in range(1,len(listOfString),1):
#         if minLength>len(listOfString[i]) and len(listOfString[i])!=0:
#             minLength=len(listOfString[i])
          

    

    
    

    # i=0
    # prefix=''
    # for j in range(0,len(str2),1):
    #     if str1[i]!=str2[j]:
    #         return prefix
            
         
    #     prefix+=str1[i]    
    #     i+=1  
            
    # return prefix    
        
        
# print(commonPrefix(["balower","ccvbabdakloao","aaa","bbb","ccc","cc",""]))

# def commonPrefix(s1,s2):
#     prefix=''
#     for i in range(min(len(s1),len(s2))):
#         if s1[i]!=s2[i]:
#             break 
#         prefix+=s1[i]
#     return prefix    
               
# print(commonPrefix("balower","bababdakloao"))
        
def longestCommonPrefix(strs):
    prefix=strs[0]
    for x in strs[1:]:
        while not str(x).startswith(prefix):
            prefix=prefix[0:(len(prefix)-1)]
            if len(prefix)==0:
                return ""
    return prefix
print(longestCommonPrefix(["flolower","flol","fl"]))