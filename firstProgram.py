print("hello world","here is my first python code")
print("my name is meherab")
a=5
b=2
print(a**b)#a power b.
A=int("2")
B=5.0
print(A+B)

name=(input("enter your name:"))
age=int(input("enter your age:"))
marks=float(input("enter your marks:"))
print("your name, age and marks na is:",name,age,marks)
#slicing
str="my name is meherab"
print((str[-5:-1]))
#ending string checkinh
print(str.endswith("ab"))
#capitalizing
print(str.capitalize()) #orginal string er korbena.new ekta copy create kore oitar first character capitalize kore dibe.
#replacing
print(str.replace("name","Name")) #original ke korbena.
print(str)
#finding
print(str.find("is"))# retunr the matching wors or characyers first index
#counting
print(str.count("is"))
age=90
if(age>=24):
    if(age>=80): #indentation or proper spacing .here 4space or 1tab.
        print("he is old please help him to vote")
    else:    
        print("can vote") 
elif(age<18):
    print("cant vote") 

number1=int(input("enter first numbers:"))
number2=int(input("enter second numbers:"))
number3=int(input("enter third numbers:"))
number4=int(input("enter 4th numbers:"))
if(number1>=number2 and number1>=number3 and number1>=number4):
    print("first number is largest :",number1)

elif(number2>=number3 and number2>=number4):
    print("second number is largest",number2)
elif(number3>=number4):
    print("third number is largest",number3)   
else:
    print("4th number is largest",number4)    