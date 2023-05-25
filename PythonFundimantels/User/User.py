class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):	
        self.account_balance += amount
    def make_withdrawl(self,amount):
        self.account_balance -= amount
    def display_balance(self):
        print(self.account_balance)


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
yazan = User("Yazan Kayed", "y.arefkayed@gmail.com")
print(yazan.name)
print(guido.name)	
print(monty.name)	

yazan.make_deposit(30000)

yazan.make_deposit(20000)

yazan.make_deposit(10000)

yazan.make_withdrawl(50)

print(yazan.account_balance)

guido.make_deposit(20000)

guido.make_deposit(10000)

guido.make_withdrawl(50)
guido.make_withdrawl(50)

print(guido.account_balance)


monty.make_deposit(20000)

monty.make_withdrawl(10000)

monty.make_withdrawl(50)
monty.make_withdrawl(50)

print(monty.account_balance)