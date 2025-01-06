numbers=[]
i=0
while(i!=6):
    numbers.append(input("enter 6 number:"))
    i+=1

print(numbers[0:])

if(numbers[0:]==numbers[::-1]):
    print("palidrome")
else:
    print("not palindrome")    