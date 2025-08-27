class atm:
    def __init(self,balance=0):
        self.pinnumber=4324
        self.balance=balance
    def verifypin(self):
        pin=int(input("enter pin"))
        pin == self.pinnumber
    def deposit(self):
        if self.verifypin():
                amount=int(input("enter amount"))
                if amount>0:
                    self.balance+=amount
                    print(amount,"added ")
                else:
                    print("invalid amount")
        else:
            print("incorrect pin")               
    def withdrawal(self):
        if self.verifypin():
            withdrawal=int(input("enter amount"))
            if withdrawal>0:
                self.balance-=withdrawal
                print(withdrawal,"withdrawel succesfull")
            else:
                print("invalid amount")
        else:
            print("incorrect pin")
    def balancecheck(self):
        if self.verifypin():
            print("balance amount = ",self.balance)
        else:
            print("incorrect pin")        
        