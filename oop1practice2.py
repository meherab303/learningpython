class Account:
    def __init__(self,bal,acc,password):
        self.balance=bal
        self.account_no=acc
        self.__passwrd=password # private attribute-->only can use within the class
    def debit(self,amount):
        self.balance-=amount
        print("total debit in your account is",amount)
        print("total balance in your account is",self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("total credit in your account is",amount)  
        print("total balance in your account is",self.get_balance())        
    def get_balance(self):
        return self.balance    
    def show_pass(self): #by doing this -->object can access private attribute outside the class.
        print(self.__passwrd)    

acc1=Account(8000,1,"abc")
acc1.debit(1000) 
acc1.credit(1000) 
(acc1.show_pass())     