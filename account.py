from datetime import datetime
class Account:
    
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
        try:
            amount+1
        except TypeError:
            print("You must enter an amount in figures") 
            return   
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
        try:
            amount+10
        except TypeError:
            print("please enter the requested amount in figures")
            return

        if amount<=0:
           print("The loan request is invalid")
        else:
            self.loan=amount
            print("You have been given a loan worth {}".format(amount))

    def repay_loan(self,amount): 
        try:
            amount+10
        except TypeError:
            print("Enter the repay in figures")
            return

        if amount==0:
            print("You Can't repay that amount")
        elif amount > self.loan:
            print("Your loan is {} please enter an amount less or equal to.".format(self.loan))

        else:
            self.loan-=amount
            time=datetime.now()
            repayment={
                "time":time,
                "amount":amount
            }
            self.loan_repayment.append(repayment)
            print("You have repaid your loan with {}.Your balance is {}".format(amount,self.loan))

    def loan_repayment_statement(self):
        for repayment in self.loan_repayments:
            time=repayment('time')
            amount=repayment['amount']
            formatted_time=self.get_formatted_time(time)
            statement="You repaid {} on {}".format(amount,formatted_time)
            print(statement)
            

#Class Inheritance
#BankAccount Inheritance
class BankAccount(Account):
    def __init__(self,first_name,last_name,phone_name,bank):
        self.bank=bank
    super().__init__(first_name,last_name,phone_name) 

#mobile money class
class MobileMoneyAccount(Account):
    def __init__(self,first_name,last_name,phone_name,service_provider):
        self.service_provider=service_provider
        self.airtime=[]
    super().__init__(first_name,last_name,phone_name)

    def buy_airtime(self,amount):
        try:
            amount+1
        except TypeError:
            print("Please enter the amount in figures")
            return

        if amount > self.balance:
            print("You dont have enough balance.Your balance is {}".format(self.balance))
        else:
            self.balance-=amount
            time=datetime.now()
            airetime={
                "time":time
                "airtime":amount
            }
            self.airtime.append(airtime)
            print("You have bought airtime worth {} on {}".format(amount,self.get_formatted_time(time)))

    def pay_bill(self,)

    def send_money(self,amount):
        self.amount=amount
        try:
            amount+1
        except TypeError:
            print("Please enter the amount in figures")
            return

        if self.amount <=0:
            print("You can't send  money of that amount")
        else:
            self.amount>0
            print("You have send an amount of {}".format(amount)


    def receive_money()
