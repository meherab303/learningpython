mysets=set()
print(type(mysets))
mysets.add(1)
#mysets.remove(1)
mysets.add((1,2,3,4))
mysets.add(2)
#mysets.clear()
#removed=mysets.pop()
#print(removed)
print(mysets)

myset2={12,1,2,3,4,5}
mysets3=myset2.union(mysets)
mysets4=mysets3.intersection(mysets)
print(mysets3)
print(mysets)
print(mysets4)


