class Account:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def deposit(self, deposit):
        self.balance+=deposit

    def withdraw(self, withdraw):
        if withdraw<self.balance:
            self.balance-=withdraw
        else:
            print ("can't perform operation")

Acc=Account("Eric", 2500)
Acc.deposit(25)
Acc.deposit(25)
Acc.deposit(25)
Acc.deposit(25)
Acc.deposit(25)
Acc.deposit(25)
Acc.withdraw(2000)
print (Acc.balance)