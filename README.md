# Bank-account
Author :- Pawan kumar
<br>
This project implements a basic Bank Account Management System using Python object-oriented programming. It allows users to perform fundamental banking operations, including depositing funds, withdrawing money, transferring funds, and checking  balances.it have a secure transaction.
<br>
# Features
Encapsulation: Uses private attributes (__bal) to protect sensitive account balance data.
Transaction Handling:
Debit: Securely deducts funds if sufficient balance is available.
Credit: Adds funds to the account balance.
Transfer: Simulates a fund transfer process requiring authentication (hardcoded password).
Interactive CLI: User-friendly command-line interface to perform banking operations.
How It Works
The script utilizes a bankaccount class to manage state. By using double underscores (__) before the bal variable, it prevents direct external access to the account balance, forcing interactions through class methods (debit, credit, transfer).
#Usage
Run the script: python bank_account.py
Enter your account number.
Follow the on-screen prompts to perform debits, credits, or transfers.
Technologies Used
Python 3.x
OOP Principles
