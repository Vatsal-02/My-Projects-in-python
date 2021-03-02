### ATM MACHINE MINI PROJECT 
### BY VATSAL PANCHAL 

import time
print('Please insert your card, Thank you')

time.sleep(2)
### giving 2 second delay after inserting card

password = 1234 
### say password is 1234
pin = int(input('Please enter your ATM pin: '))

balance = 5000
### this is my account balance

if pin == password:
    while True:
        print('\n1 = View Balance\n2 = Withdraw Balance\n3 = Deposit Money\n4 = Exit')

        try:
            option = int(input('Please enter your choice: '))
        except:
            print('Please enter a valid option')

        if option == 1:
            print('\nYour balance is: Rs.', balance, '\nHave a nice day \nThank you')
            break


        elif option == 2:
            withdrawal_amount = int(input('Please enter your withdrawal amount: '))
            balance = balance - withdrawal_amount
            print('--------------------------------------------------------------')
            print('\nRupee',withdrawal_amount,'has been debited from your account.')
            print('\nYour current bank balance is: Rs.',balance)
            print('\nHave a nice day\nThank you')
            break



        elif option == 3:
            deposit_amount = int(input('Please enter your deposit amount: '))
            balance = balance + deposit_amount
            print('--------------------------------------------------------------')
            print('\nRupee',deposit_amount,'has been credited in your account.')
            print('\nYour current bank balance is: Rs.',balance)
            print('\nHave a nice day\nThank you')
            break

        else:
            break
else:
    print('\n\nPlease enter a valid Pin. \nThank you')
