class BankAccount:
  def __init__(self, account_number, balance = 0):
    self.balance = balance
    self.account_number = account_number
    
  def depositAmount(self, deposit = 0):
    self.balance += deposit
  
  def depositWithdrawal(self, withdrawal = 0):
    self.balance -= withdrawal
  
  def transfer_funds(self, transferNewAccount, otherAccount):
    self.balance -= transferNewAccount
    otherAccount += otherAccount + transferNewAccount

  
  

wellsFargo = BankAccount(4444444,20000)
# print(vars(wellsFargo))
# wellsFargo.depositAmount(50000)
# print(vars(wellsFargo))

# print(wellsFargo.balance)
wellsFargo.transfer_funds(500, 200)
# print(vars(wellsFargo))
wellsFargo.transfer_funds(500, 200)
print(vars(wellsFargo))
print(wellsFargo.balance)