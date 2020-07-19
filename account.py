class BankAccount:
    bank="KCB"
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
        self.balance=0

    def accountName(self):
        name="{} account for {} {}".format(self.bank,self.firstName,self.lastName)
        return name

    def deposit(self,amount):
        self.balance+=amount
        print("You have deposited {} to your account".format(amount))

    def getBalance(self):
        return "The balance for {} is {}".format(self.accountName(),self.balance)

    def withdraw(self,cash):
        self.cash=cash
        print("You have withdrawn {} amount from your account".format(self.cash))

acc1=BankAccount("Annita","Wanjiru")
acc2=BankAccount("Komo","Brian")
acc1.deposit(-100)
acc1.deposit(7500)
acc2.deposit(2000)
acc2.deposit(50)
print(acc2.accountName())
print(acc1.accountName())
print(acc1.getBalance())
print(acc2.getBalance())
print(acc1.withdraw(600))

