class BankAccount:
    
    def __init__(self,first_name,last_name,bank,phone_number):
        self.first_name=first_name
        self.last_name=last_name
        self.balance=0
        self.bank=bank
        self.phone_number=phone_number
        self.deposit=[]
        self.withdrawals=[]
        self.loan=0

    def account_name(self):
        name="{} account for {} {}".format(self.bank,self.first_name,self.last_name)
        return name

    def deposit(self,amount):
        if amount<=0:
           print("You cannot deposit zero or negative")
        else:
            self.balance+=amount
            self.deposit.append(amount)  
            print("You have deposited {} to {}".format(amount,self.account_name()))


    def withdraw(self,amount):
        if amount<=0:
            print("You cannot withdraw zero or a negative")

        elif amount > self.balance:
            print("You dont have enough balance")
        else:
            self.balance==amount
            self.withdrawals.append(amount)
            print("You have withdrawn {} from {}".format(amount,self.accont_name()))    
    
    def get_balance(self):
        return "The balance for {} is {}".format(self.accountName(),self.balance)
    
    def show_deposit_statement(self):
        for deposit in self.deposits:
            print(deposit)

    def show_withdrawals_statement(self):
        for withdrawal in self.withdrawals:
            print(withdrawal)

      
    def request_loan(self,amount):
        if amount<=0:
           print("The loan request is invalid")
        else:
            self.loan=amount
            print("You have been given a loan worth {}".format(amount))

    def repay_loan(self,amount): 
        if amount<=0:
            print("Can't repay that amount")
        elif:
            amount>self.loan
            print("Your loan is {} please enter an amount less or equal to.".format(self.loan))

        else:
            self.loan=>amount
            print("You have repaid your loan with {}.Your balance is {}".format(amount,self.loan))
