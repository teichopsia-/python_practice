# Calculates the minimum fixed monthly payment needed to pay off
# a credit card balance within 12 months.
def minimumPayment(balance=3329, annualInterestRate=0.2):
    '''
    Returns the minumum fixed amount needed to pay off a Credit Card
    payment within 12 months.
    #! missing type checker / assert statements for:
        balance
        annualInterestRate
    '''
    unpaid_balance = 0
    min_pay = 0  # += 10
    monthlyInterestRate = annualInterestRate / 12.0
    old_balance = balance

    while unpaid_balance < balance:
        min_pay += 10
        balance = old_balance
        for month in range(1, 13): 
            
            unpaid_balance = balance - min_pay
            balance = unpaid_balance  #update the old balance with new balance.
            interest = monthlyInterestRate * balance
            balance += interest
    print 'Lowest Payment: {}'.format(min_pay)
