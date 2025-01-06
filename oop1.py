class Webdevelopment: # class name always start with capital letter.it is naming convention
    prerequisite="full stack" # class attribute


    def __init__(self,position,salary): #constructor --> use for object attribute initializatation
        self.position=position  # instance attribute
        self.salary=salary # instance attribute


        

    def welcome_ph(self):  # method(non-static-method) --> can access objects all properties.alwayes self parameter dite hbe
        print(self.prerequisite,"shohoj shorol simple assignment e apnake shagotom")



    @staticmethod # decorator--> is a function that take input as a function and give out as a function withour modifiying the taken function.        
    def print_hello():
        print("workd hard untill your dream is fullfilled")

employer_one=Webdevelopment("senior Instructor",25000) #creating object
employer_Two=Webdevelopment("junior Instructor",15000)

print(employer_one.position)
print(employer_Two.salary)
print(Webdevelopment.prerequisite) #class attribute ke access korte class.attribute korleo hoi.
employer_one.welcome_ph() 
employer_one.print_hello() 