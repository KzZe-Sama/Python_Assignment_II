class BankingApplication:
    def __init__(self, CustomerID, CustomerName, CustomerAddress, Email, Phone, BankNumber, BankBalance):
        self.CustomerID = CustomerID
        self.CustomerName = CustomerName
        self.__CustomerAddress = CustomerAddress
        self.__Email = Email
        self.__Phone = Phone
        self.__BankNumber = BankNumber
        self.__BankBalance = BankBalance

    # Loading Balance
    def deposit(self, balance):
        dummy=self.__BankBalance
        self.__BankBalance = self.__BankBalance + balance
        return f"Old Balance: {dummy:,.2f}\n{balance} Deposited\nNew Balance: {self.__BankBalance:,.2f}"

    # Withdrawing Balance
    def withdraw(self, balance):
        if balance> self.__BankBalance:
            return "In-sufficient Funds in Bank Account"
        else:
            dummy = self.__BankBalance
            self.__BankBalance = self.__BankBalance - balance
            receipt = f"{dummy:,.2f} - {balance:,.2f} = {self.__BankBalance:,.2f}"
            return receipt


# Work Later on transfer and other methods

A = BankingApplication(101, "Vidur Khanal", "Gongabu", "abc@xyz.com", "975-444-3456", 100923124, 10000)
# Deposit Money
print(A.deposit(9000))

# Withdraw Money
print(A.withdraw(1000))

