class atm:
    def __init__(self):
        self.pinnumber=4324
        self.balance=0
    def verifypin(self):
        pin=int(input("enter pin"))
        if pin == self.pinnumber:
            return True
        else:
            return False
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
    def choise(self):
        while(True):
            print('''1.deposit
                 2.withdrawal
                 3.balance
                 4.exit''')
            choise=int(input("enter choise : "))    
            if choise==1:
                self.deposit()
            elif choise==2:
                self.withdrawal()
            elif choise==3:
                self.balancecheck()
            elif choise==4:
                break
            else:
                print("invalid input")
test=atm()
test.choise()
            