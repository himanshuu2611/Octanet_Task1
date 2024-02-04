import time

# set password for logging
password = 4321
card_no = int(input("please enter your CARD : "))
pin = int(input("enter your pin : "))
time.sleep(1)
# set balance for transactions
balance = 5000

if pin == password and type(card_no) == int:
    while True:
        print("""
    1== balance
    2==withdraw
    3==deposit
    4==exit
    """)
        try:
            option = int(input("please enter your choice : "))
        except:
            print("please enter valid value")

        if option == 1:
            print(f"your current balance : {balance}")
        if option == 2:
            withdrawal_amount = int(input("enter withdrawal amaount : "))
            if withdrawal_amount > balance:
                print("Sorry ! ,Insufficient balance")
            else:
                balance = balance - withdrawal_amount
                print(f"{withdrawal_amount} is debited from account")
                print(f"your updated  balance : {balance}")

        if option == 3:
            deposit_amount = int(input("enter your amount to deposit : "))
            balance = balance + deposit_amount
            print(f"{deposit_amount} is credited in your account")
            print(f"your updated balance : {balance}")

        if option == 4:
            print("""
        Thank you for using me 
        Please visit again !
        """)
            break

        if option>4:
            print("please select correct option.")


else:
    print("invalid pin ")
