# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Create a class called 'BankAccount' to represent a bank account. The class should have the following attributes and methods:

Attributes:
- 'account_number': a string representing the account number.
- '__balance': a float representing the current balance of the account. It must be private

Methods:
- 'deposit(amount)': a method that adds the provided amount to the account balance.
- 'withdraw(amount)': a method that subtracts the provided amount from the account balance.
- 'get_balance()': a method that returns the current balance of the account.

Create an instance of the 'BankAccount' class with your own account information and demonstrate the usage of the methods.

"""


### Define the BankAccount class


### TEST:
# account1 = BankAccount("12345", 1000.0)
# account1.deposit(500.0)
# account1.withdraw(200.0)
# print(account1.get_balance())

# # Attempt to directly modify the balance (no effect, as __balance is private):
# account1.__balance = 0
# print(account1.get_balance())

### EXPECTED OUTPUT:
# 1300.0
# 1300.0