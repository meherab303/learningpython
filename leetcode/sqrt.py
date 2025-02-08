def sqrt(X):
    if X==0:
        return 0
    i=1
    while pow(i,2)<=X:
        i+=1
    
        
    if pow(i,2)==X:
           
            return i    
            
    # y=pow(i,2)
    # z=pow(i-1,2)
    # if y-X>X-z:
    #     print(X-y>X-z)
    #     return i-1
    # else:
    #     return i       
    
    return i-1
              
              
print(sqrt(36))            