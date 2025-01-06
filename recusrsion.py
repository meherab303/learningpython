
def sum(n):
    
    if(n==1):
        return 1
    
    return sum(n-1)+n


#print(sum(6))

list=["dhaka","cumilla","rajshahi","ctg"]


#length=0
"""def print_cities(list):
    global length
   
    print(list[length])
    length+=1
    if(length==(len(list))):
        return

    print_cities(list) """


def print_cities(list,length=0):
    if(length==(len(list))):
        return
    
    print(list[length])
    print_cities(list,length+1) 



print_cities(list)       