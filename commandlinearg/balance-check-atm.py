import sys
lst = sys.argv
accBalance = 10000
choice = int(lst[1])
if choice == 1: print("Balance: Rs.",accBalance)
elif choice == 2:
    amm = int(input("Enter amount to withdraw: Rs."))
    if amm>accBalance:
        print("Low Balance")
        exit()
    else: accBalance -= amm
    print("Amount Deducted: Rs.",amm)
    print("New Balance: ",accBalance)
elif choice == 3:
    amm = int(input("Enter amount to Deposit: "))
    accBalance += amm
    print("Amount Deposited: Rs.", amm)
    print("New Balance: ", accBalance)
elif choice == 4:
    amm = int(input("Enter check amount to Deposit: "))
    accBalance += amm
    print("Check Deposited of amount: Rs.", amm)
    print("New Balance: ", accBalance)
else: print("Invalid Choice")