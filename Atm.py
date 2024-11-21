import time

print("Please insert Your CARD")

time.sleep(5)

password = 1234

pin = int(input("enter your atm pin "))

balance = 5000

if pin == password:
    while True:
        
        print("""
            1 == balance
            2 == withdraw balance
            3 == deposit balance
            4 == exit
            """
              )

        try:
            choice = int(input(" Please enter your choice:"))
        except:
            print("Please enter valid choice ")

        if choice == 1:
            print(f"Your current balance is {balance} ")

        if choice == 2:

            withdraw_amount = int(input("please enter withdraw_amount"))

            balance = balance = withdraw_amount

            print(f"{withdraw_amount} is debited from your account")

            print(f"Your current balance is {balance} - {withdraw_amount}")

        if choice == 3:

            deposit_amount =int(input("please enter deposit_amount"))

            balance = balance + deposit_amount

            print(f"{deposit_amount} is credited to your account")

            print(f"your updated balance is {balance}")

        if choice == 4:

            break 

else:
    print("Invalid Pin")