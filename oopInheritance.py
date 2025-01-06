# single and multilevel inheritace
class Car:
    @staticmethod # static method shokol instance er jonno same e thake .karon eita kono attribute access korena.so eitake attribute diye change o kora jabena .
    def start():
        print("car is starting..")
    @staticmethod # static method tokhn e create korbo jokhn class ba instance attribute er access er dorkar na hoi
    def stop():
        print("car is stopped..")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand
    @staticmethod
    def start():
        print("car is starting..")        
    def setCc(self,cc):
        self.cc=cc
       # return self.cc jdi super er maddome na initialize korte chai.
    def getCC(self):
        return self.cc
         
           
class Fortuner(ToyotaCar):
    def __init__(self, type,brand,cc):
        self.type=type
        #self.cc=cc  --> eita likhle Fortuner class er attribute set hoye jabe.
        super().setCc(cc) # eitar maddome ami parent class ke call kore parent class er attribute set kore dilam
        super().__init__(brand) # call the parent class or contructor to initialize the brand 
        super().start() # er maddome jokkhn e fortuner er object create hbe tokhn e stat method call hoye jabe karon constructor object create er sathe sathei call hoye jai automatic.
        #super diye only immediate parent class ke call kora jai. 

car1=Fortuner("electric","toyota",1500)  

print(car1.brand)
print(car1.type)  
#print(car1.setCc(1500))
print(car1.getCC()) 
 


#multiple inheritance
class A:
    var1="this is class A"
class B:
    var2="this is class B" 
class C(A,B):
    var3="this is class c"       
varr=C()
print(varr.var1,varr.var2,varr.var3)   


# class methods

class Person:
    name="anonymouse"

    #def changeName(self,name): # eita object er modde name create kore notun kore.Person class er name ke change korena.
        #self.name=name
    #def changeName(self,name):
       # Person.name=name #eibhabe person class er name change kora jabe 
        #self.__class__.name=name # eibhabeo kora jabe.

    @classmethod #othoba classmethod(decorator) use koreo kora jabe.class method class attribute access kore only.

    def changeName(cls,name):
        cls.name=name
p1=Person()
p1.changeName("nahin")
print(p1.name)
print(Person.name)

# types of methods
#1.static methods-->kono attribute e access korte parena.jokhn class ba instance attribute er konotai access er droker porbena tokhn amora staticmethods use korbo
#2.class methods-->only class attribute access kore.prothom argument hoy cls ba class.only class attribute modify korte chaile use korbo
#3.instance methods--> only instance attribute access kore.prothom attribute hoi self.instance er attribute initialize/modify korte use hoi


#property decorator...(important)

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        #self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
        #self.percentage=str((math+phy+chem)/3)
    @property #This decorator makes the method calculatePercentage behave like an attribute.You can access it without parenthesess1.calculatePercentage instead of s1.calculatePercentage()
    def calculatePercentage(self): # jotober eitake access kora hobe totobar notunkore calculate hobe.tai value pore change koreo ei function ke access korte chaile updated value ashbe.
        return  str((self.math+self.phy+self.chem)/3)     

s1=Student(98,98,98)
print(s1.calculatePercentage)
s1.math=96
print(s1.math)
print(s1.calculatePercentage)

""""Explanation:
@property Decorator:

This decorator makes the method calculatePercentage behave like an attribute.
You can access it without parentheses (s1.calculatePercentage instead of s1.calculatePercentage()).
Method Definition:

calculatePercentage is defined as a method but behaves like an attribute when accessed.
Every time calculatePercentage is accessed, the code inside it executes dynamically.
Dynamic Calculation:

The method calculates the average of self.math, self.phy, and self.chem dynamically. If any of these attributes change, the new value will automatically be used in the calculation."""
       