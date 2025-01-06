class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for value in self.marks:
            sum+=value    
        print("hi",self.name,"your avg score is",sum/3,end="") 
    @staticmethod       
    def motivation():
        print("dont compete with others.You need to be better than is the person you were yesterday")


s1=Student("arya",[98,98,98])
s1.get_avg()
s1.name="sansa"
s1.get_avg()
s1.motivation()