
class bankaccount:
    bankname= None
    def __init__(self,name,acnumber,balance=0):
        self.name=name
        self.acnumber=acnumber
        self.balance=balance
        print("name :",self.name  ,'|' 'acnumber : ',self.acnumber,'|','balance :',self.balance)

    def deposit(self,amount):
        self.balance+=amount
        print(f"Your account credited {amount}. New balance is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print(f"Your account debited {amount}. New balance is {self.balance}")
    
    def checkbalance(self):
        print(f"Your current balance is {self.balance}")

    @classmethod
    def bankname(cls,bankname):
        cls.bankname=bankname
        print(f"Welcome to {cls.bankname} bank")
    
    @staticmethod
    def validateaccountnumber(acnumber):
        if len(str(acnumber))==10:
            print("Valid account number")
        else:
            print("Invalid account number")

    
# accout =bankaccount('jay',1234567890,5000)

# accout.bankname('icici')

# accout.deposit(2000)

# accout.withdraw(1000)

accout1 =bankaccount('jay',12345670,5000)

accout1.bankname('icici')

accout1.deposit(2000)

accout1.withdraw(1000)

accout1.validateaccountnumber(12345670)
