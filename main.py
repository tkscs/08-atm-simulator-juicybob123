#we start with 1,000,000 dollars
y = 2
x = 1
while y == 2:
    who = int(input("please input 1 if you wanna play as bill gates, input 2 if you want to play as yoni, or 3 if you wanna play as default"))
    if who == 1:
        balance = 103000000000
        print("you successfully are playing as bill gates")
        y = 3
    elif who == 2:
        balance = 12
        print("you successfully are playing as yoni")
        y = 3
    elif who == 3:
        balance = 1000000
        print("you successfully are playing as default")
        y = 3
    else:
        print("please pick 1, 2, or 3.")
while x >= 0.5:     
    promt = (input("pick From either withdraw, check your balance, or deposit money\n"))
    if promt == ("withdraw"):
        withdrawing = int(input("please input the amount of money you want to withdraw\n"))
        if withdrawing <= balance and withdrawing >= 1:
            balance = balance - withdrawing
            print(f"your new balance is {balance}")
        else:
            print("you will go to jail for fraud")
    if promt == ("balance"):
        print (f"your balance is {balance}")
    if promt == ("deposit"):
        promqt = int(input("please enter the amount of money you want to deposit\n"))
        if promqt >= 1:
            balance = balance + promqt
            print(f"success. Your new balance is {balance}")
        else:
            print("you dirty fraud trying to scam the system")