"""Basic bank account"""
class bankaccount:
    def __init__(self, acc_no, bal):
        self.acc_no = acc_no
        self.__bal = bal
    
    def debit(self, amount):
        if (0 < amount <= self.__bal):
            self.__bal -= amount
            print(amount,"are debited in your account.")
            print(self.__bal,"are your balance.")
        else:
            print("YOU HAVE NOT ENOUGH MONEY FOR DEBIT AMOUNT IN YOUR ACCOUNT.")
            
    def credit(self, amount):
        self.__bal += amount
        print(amount,"amount are created in your account.")
        print(self.__bal,"are your balance.")
        
    def transfer(self, amount):
        e = int(input("Enter acc_no to send money:"))
        pas = int(input("Enter your password:"))
        if (pas == 12345678):
            print(amount,"are transferred successfully.")
            self.__bal -= amount
            print(self.__bal,"are your balance.")
        else:
            print("YOUR PASSWORD IS WRONG!!!")
            
a = int(input("Enter acc_no :"))
c1 = bankaccount(a, 10000)
b = int(input("Enter amount you want debit:"))
c1.debit(b)
c = int(input("Enter amount you wnat credit:"))
c1.credit(c)
f = input("If you want transfer money than write (yes) or if not than write (no):")
if (f == "yes"):
    amount = int(input("Enter amount you want transfer money:"))
    c1.transfer(amount)
else:
    print("OK, THANK YOU FOR USING MY SERVICE.")
