def climbingStairs(n):
    if n<=2:
        return n
    listt={}
   
    listt[1]=1
    listt[2]=2
    

    for i in range(3,n+1,1):
        listt[i]=listt[i-1]+listt[i-2]
        
    
    return listt[n]    

print(climbingStairs(10))