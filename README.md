# Bank-account
Author :- Pawan kumar
<br>
This project implements a basic Bank Account Management System using Python object-oriented programming. It allows users to perform fundamental banking operations, including depositing funds, withdrawing money, transferring funds, and checking  balances.it have a secure transaction.
<br>
# Features
<br>
<b> Encapsulation </b>: Uses private attributes (__bal) to protect sensitive account balance data.

# Transaction Handling:

<b> Debit </b>: Securely deducts funds if sufficient balance is available.
<b> Credit </b>: Adds funds to the account balance.
<b> Transfer </b>: Simulates a fund transfer process requiring authentication (hardcoded password).
<b> Interactive CLI </b>: User-friendly command-line interface to perform banking operations.

# How It Works

The script utilizes a bankaccount class to manage state. By using double underscores (__) before the bal variable, it prevents direct external access to the account balance, forcing interactions through class methods (debit, credit, transfer).

# Usage

<b> Run the script </b> : python bank_account.py
Enter your account number.
Follow the on-screen prompts to perform debits, credits, or transfers.
Technologies Used
<br>
<b> Python 3.x
OOP Principles </b>
