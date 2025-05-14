
def balance(balance):
    print(f'Your balance is £{balance:.2f}')

# Program which adds an amount of money to the user's bank balance
def deposit():
    amount = float(input('Please enter an amount of money'))
    
    if amount < 0:
        print('Please ensure your deposit is greater than zero') # program checks for user input errors
        return 0 
    else:
        return amount

# Program which removes an amount of money from a user's bank balance
def withdrawal(balance):
    amount = float(input('Please enter an amount of money'))

    if amount > balance:
        print('Please ensure your withdrawal is less than your bank balance') # program checks for user input errors
        return 0
    elif amount < 0: 
        print('Please ensure the withdawal is greater than zero')
        return 0
    else:
        return amount 

# The ATM program, allowing the user to add or withdraw money from their bank account
def ATM_program():
    balance = 0 
    programrunning = True 

    print('Welcome to our banking services. Select an option to continue.')
    while programrunning:
        print(f'Your balance is currently £{balance} \n')
        print('Select an option to proceed:\n')
        userchoice = input('1 - Make a deposit \n 2- Make a withdrawal \n 3 - Exit Program')

        if userchoice == '1':
            balance += deposit() # the deposit program runs, allowing the user to define a deposit
            answer1 = input('Do you wish to make another transaction? (Y/N)')
            if answer1 == 'N':
                programrunning = False
        elif userchoice == '2':
            balance -+ withdrawal(balance) # the withdrawal program runs, allowing the user to define a withdrawal
            answer2 = input('Do you wish to make another transaction? (Y/N)')
            if answer2 == 'N':
                programrunning = False
        elif userchoice == '3':
            programrunning = False
        else:
            print('Please select a number between 1 and 3') # user input error

    print(f'Your final balance was £{balance} \n')
    print('Thank you for using our banking services. We hope you have a good day')
    
#  It is possible, within ATM_program, to combine user choices '1' and '2,'so that deposit() runs if the amount of money defined is positive, and withdrawal() runs if the amount of money defined is negative. However, this is not how real ATMs work, and so was not done
