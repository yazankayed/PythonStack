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



guido = BankAccount(1000, 0.2)
monty = BankAccount(9000, 0.6)
yazan = BankAccount(5000, 0.8)
	

yazan.make_deposit(30000).make_deposit(20000).make_deposit(10000).make_withdrawl(50).display_balance()

guido.make_deposit(20000).make_deposit(10000).make_withdrawl(50).make_withdrawl(50).display_balance()

monty.make_deposit(20000).make_withdrawl(10000).make_withdrawl(50).make_withdrawl(50).yield_interest(0.2).display_balance()





