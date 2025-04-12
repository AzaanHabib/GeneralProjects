
def balance(balance):
    print(f'Your balance is £{balance:.2f}')

# Program which adds an amount of money to the user's bank balance
def deposit():
    amount = float(input('Please enter an amount of money'))

    if amount < 0:
        print('Please ensure your deposit is greater than zero')
        return 0 
    else:
        return amount

# Program which removes an amount of money from a user's bank balance
def withdrawal(balance):
    amount = float(input('Please enter an amount of money'))

    if amount > balance:
        print('Please ensure your withdrawal is less than your bank balance')
        return 0
    elif amount < 0: 
        print('Please ensure the withdawal is greater than zero')
        return 0
    else:
        return amount 

# The ATM program, allowing hte user to add or withdraw money from their bank account
def ATMprogram():
    balance = 0 
    programrunning = True 

    print('Welcome to our banking services. Select an option to continue.')
    while programrunning:
        print(f'Your balance is currently £{balance} \n')
        print('Select an option to proceed:\n')
        userchoice = input('1 - Make a deposit \n 2- Make a withdrawal \n 3 - Exit Program')

        if userchoice == '1':
            balance += deposit()
            answer1 = input('Do you wish to make another transaction? (Y/N)')
            if answer1 == 'N':
                programrunning = False
        elif userchoice == '2':
            balance -+ withdrawal(balance)
            answer2 = input('Do you wish to make another transaction? (Y/N)')
            if answer2 == 'N':
                programrunning = False
        elif userchoice == '3':
            programrunning = False
        else:
            print('Please select a number between 1 and 3')

    print(f'Your final balance was £{balance} \n')
    print('Thank you for using our banking services. We hope you have a good day')
