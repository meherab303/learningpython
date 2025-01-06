

nums=[1,2,3,4,4,5,5,6,7,7,9,6,7,78]
x=78
i=0
for val in nums:
    
    if(val==x):
        print("number found at idx",i)
        break
    i+=1

print(range(5)) 

n=5
sum=1
    
for el in range(1,n+1):
    print(el)
    sum*=el

print(sum)
