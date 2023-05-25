class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self
    def make_withdrawl(self,amount):
        self.account_balance -= amount
        return self
    def display_balance(self):
        print(self.account_balance)


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
yazan = User("Yazan Kayed", "y.arefkayed@gmail.com")
	

yazan.make_deposit(30000).make_deposit(20000).make_deposit(10000).make_withdrawl(50).display_balance()

guido.make_deposit(20000).make_deposit(10000).make_withdrawl(50).make_withdrawl(50).display_balance()

monty.make_deposit(20000).make_withdrawl(10000).make_withdrawl(50).make_withdrawl(50).display_balance()





