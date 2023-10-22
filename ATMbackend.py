#Backend ATM Application
'''
  1. Check Balance 
  2. Withdraw Amount 
  3. Deposit Money 
  4. Change pin
  5. Transaction History
  6. Exit (ask confirmation)
'''
import datetime
pin = 1234
balance = 5000
transactions = []
#current_time = datetime.datetime.now() #caused all time values to be the same.
print("Welcome to ATM...")

def transac(ch,content,balance):
    if ch==1:
        transactions.append(["Checked balance", content, balance, datetime.datetime.now()])
    if ch==2:
        transactions.append(["Cash withdrawn ", f"-{content}", balance, datetime.datetime.now()])
    if ch==3:
        transactions.append(["Cash deposited ", f"+{content}", balance, datetime.datetime.now()])

def transac_display():
    if transactions == []:
        print("No transaction history recorded yet.")
    else:    
        print("---------------------------------------------------------------------------------------------------")
        print("|Action\t\t\t|Amount\t\t\t|Remaining balance\t|Date/Time")
        print("---------------------------------------------------------------------------------------------------")
        
        for i in transactions:
            print(f"|{i[0]}\t|{i[1]}\t\t\t|{i[2]}\t\t\t|{i[3]}")
        print("---------------------------------------------------------------------------------------------------")
        
while True:
    validation=int(input("Enter pin: "))
    if validation!=pin:
        print("Invalid Pin")    
        break
    else:
        print("Choose option\n1. Check Balance\n2. Withdraw Amount \n3. Deposit Money \n4. Change pin \n5. Transaction History\n6. Exit")
        print("===============================")
        choice = int(input("Enter choice: "))
        if choice==1:
            print("Balance:",balance)
            transac(1,balance,balance)
            
        elif choice==2:
            withdraw = int(input("Enter amount to withdraw: "))
            if withdraw>balance:
                print("Insufficient Balance.")
            else:
                balance-=withdraw
                print(withdraw,"withdrawn, balance:",balance)
                transac(2,withdraw,balance)
        elif choice==3:    
            deposit = int(input("Enter amount to deposit: "))
            balance+=deposit
            print(deposit,"deposited, balance:",balance)
            transac(3,deposit,balance)
        elif choice==4:
            validation=int(input("Enter current pin: "))
            if validation==pin:
                print("Pin changed to",pin)
            else:
                print("Incorrect pin. Pin change request denied.")
        elif choice==5:
            transac_display()
        elif choice==6:
            print("Do you want to exit(Y/N) ", end = '')
            exitbool = input()
            if exitbool=='N' or exitbool=='n':
                continue
            if exitbool=='Y' or exitbool=='y':
                print("Thank you for using ATM")
                break
        else:
            print("Please Enter Valid Choice")
        print("===============================")

