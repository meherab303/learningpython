#with open("practice.txt","w") as f:
    #f.write("hi everyOne\nwe are learning file i/o\nusing Java\ni like using Java")

with open("practice.txt","r") as f:
    data=f.read()
new_data=data.replace("Java","python")
#print(new_data)


"""with open("practice.txt","w") as f:
    f.write(new_data)

def check_word(w):
    with open("practice.txt","r") as f:
        data=f.read()
        if(data.find(w)!=-1):
            print("Found")
        else:
            print("not found") """   


#check_word("learning")   


def check_for_line(word):
    data=True
    lineNumber=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(lineNumber)
                return
            lineNumber+=1
    return -1        


#print(check_for_line("like"))    

count=0
with open("practice.txt","r") as f:
    data=f.read()
    print(data)
    
    nums=""
    for i in range(0,len(data)):
        if(data[i]=="," ):
            if(int(nums)%2==0):
                print(nums,"is even number")
                count+=1
            nums=""
        else:
            nums+=data[i]    

print("total odd number is ",count)  
count=0
with open("practice.txt","r") as f:
    data=f.read()
    numbers=data.split(",")
    print(numbers)
    
    for value in numbers:
        if(value==""):
            print("number is end")
            break
            
        if(int(value)%2==0):
            count+=1
            print(int(value),"is even number")

print("total even numbers is",count)    
