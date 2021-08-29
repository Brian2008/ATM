class ATM(object):
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        

    def cashWithdrawl(self): 
        print("You have withdrawn your cash!")
    def BalanceEnquiry(self):
        print("You have alot of money in your bank account")


atm1 = ATM("11111", "22222")
print(atm1.cardNumber)
atm1.cashWithdrawl()
atm1.BalanceEnquiry()