class BankAccount:
    def get_balance(self):
        return self.__balance
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.__balance = balance
    def deposit(self,amount):
        self.__balance = self.__balance + amount
    def withdraw(self,amount):
        if amount > self.__balance:
            print("insufficient balance")
        else:
            self.__balance =  self.__balance - amount
class SavingsAccount(BankAccount):
    def __init__(self,account_number,balance,interestrate):
        super().__init__(account_number,balance)
        self.interestrate = interestrate
    def calculate_interest(self):
        balance = self.get_balance()
        interest = balance * self.interestrate
        return interest
class CurrentAccount(BankAccount):
    def __init__(self,account_number,balance,minimum_balance):
        super().__init__(account_number,balance)
        self.minimum_balance = minimum_balance
    def withdraw(self,amount):
        balance = self.get_balance()
        if amount > balance:
            print("insufficient balance")
        elif balance -  amount < self.minimum_balance:
            print("minimum balance violation")
        else:
            super().withdraw(amount)
            
#hardcoded example for testing

acc = BankAccount(101,1000)
acc.deposit(500)
acc.withdraw(200)

sav = SavingsAccount(102,2000,0.5)
print(sav.calculate_interest())

curr = CurrentAccount(103,3000,1000)
curr.withdraw(2500)

acc = BankAccount(101,1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())
    






    


