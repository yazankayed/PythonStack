class BankAccount:
    def __init__(self, balance, int_rate):
        self.int_rate=int_rate
        self.account_balance = balance
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self
    def make_withdrawl(self,amount):
        self.account_balance -= amount
        return self
    def display_balance(self):
        print( "Balance: $", self.account_balance)
    def yield_interest(self,intrstRate):
            self.account_balance=self.account_balance*(intrstRate+1)
            return self



class User:		
    def __init__(self, name, email,balance,int_rate):
        self.name = name
        self.email = email
        self.account =  BankAccount(balance,int_rate)
        self.user=User(name, email,balance,int_rate)              #list of objects in python
    # def make_deposit(self, amount):	
    #     self.account += amount
    #     return self
    # def make_withdrawl(self,amount):
    #     self.account -= amount
    #     return self
    # def display_balance(self):
    #     print(self.account)
    #     return self


yazan=User("yazan","jkfrjkkvdfjjkdf",1000,0.02)

yazan.account.make_deposit(50).display_balance()



