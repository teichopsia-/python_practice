# Write a program to calculate the CC balance after one year if a 
# person only pays the minimum monthly payment required by the CC
# company each month
def credit_card_payment(balance=4842, annualInterestRate=0.2,
                        monthlyPaymentRate=0.04):
    '''
    Returns the total payed on interest for a credit card and
    the remaining balance
    #! missing type checker / assert statements for:
        balance
        annualInterestRate
        monthlyPaymentRate
    '''
    total_payed = 0
    for month in range(1, 13): 
        min_pay = balance * monthlyPaymentRate
        unpaid_balance = balance - min_pay
        balance = unpaid_balance
        interest = (annualInterestRate / 12.0) * balance
        balance += interest
        total_payed += min_pay
        print 'Month: {}'.format(month)
        print 'Minimum monthly payment: {}'.format(round(min_pay, 2))
        print 'Remaining balance: {}'.format(round(balance, 2))

    print 'Total paid: {}'.format(round(total_payed, 2))
    print 'Remaining balance: {}'.format(round(balance, 2))
