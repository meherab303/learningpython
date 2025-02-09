def sqrt(X,precision=2):
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
    # i-=1
    # increment = 0.1
    # for _ in range(precision):  # Adjust the number of decimal places
    #     while (i + increment) * (i + increment) <= X:
    #         i += increment
    #     increment /= 10  # Reduce increment for more precision

    # return round(i, precision)  # Return rounded result

              
              
print(sqrt(2))            