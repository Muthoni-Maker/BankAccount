class BankAccount:
    
    def __init__(self,first_name,last_name,bank,phone_number):
        self.first_name=first_name
        self.last_name=last_name
        self.balance=0
        self.bank=bank
        self.phone_number=phone_number

    def account_name(self):
        name="{} account for {} {}".format(self.bank,self.first_name,self.last_name)
        return name

    def deposit_statement(self,amount):
        self.balance+=amount
        print("You have deposited {} to your account".format(amount))

    def get_balance(self):
        return "The balance for {} is {}".format(self.accountName(),self.balance)

    def withdraw_statement(self,cash):
        self.cash=cash
        print("You have withdrawn {} amount from your account".format(self.cash))

    def loan(self,loan_amount):
         self.loan=loan_amount
         print("You have been given a loan worth {}".format(loan_amount))

    def repay_loan(self):
        self.pay+=loan_amount
        print("You have paid your loan of amount {}".format(loan_amount))
