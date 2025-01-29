class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def get_details(self):
     
        return f" Title:{self.title},Author:{self.author},price:{self.price}"
    def discount(self,discount_percentage):
        if 0<=discount_percentage<=100:
             self.price=self.price*(discount_percentage/100)
        else:
            print("Invalid discount percentage")    
       


        