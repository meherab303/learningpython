f=open("demo.txt","r")
data=f.read()
line1=f.readline()
line2=f.readline()
#print(line1)
#print(data)
f.close()
f1=open("demo.txt","r")
lines=f1.readline()
#print(lines)
f.close()
f1=open("demo.txt","a+")
f1.write("amarn")
print(f1.read())
f.close()
with open("demo.txt","r") as f:
    data=f.read()
    print(data)
# with diye korle last e close korte hoina.close na korle default hishebe close hoye jai
import os
os.remove("sample.txt")