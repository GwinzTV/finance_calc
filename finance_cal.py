class FinanceCalculator:
    '''
    This finance calculator library can be used to perform common financial calculations, such as:
    Compound interest, Simple interest, Present value, Annuity payment.
    '''
    def __init__(self):
        pass
    
    def compound_interest(self, principal, rate, time):
        '''
        Calculate compound interest.
        
        Args:
            principal (float): The initial amount of money.
            rate (float): The annual interest rate (as a decimal).
            time (int): The time the money is invested for (in years).
        
        Returns:
            float: The amount of money after compound interest.
        '''
        return principal * (1 + rate)**time
    
    def simple_interest(self, principal, rate, time):
        '''
        Calculate simple interest.
        
        Args:
            principal (float): The initial amount of money.
            rate (float): The annual interest rate (as a decimal).
            time (int): The time the money is invested for (in years).
        
        Returns:
            float: The amount of money after simple interest.
        '''
        return principal * (1 + rate * time)
    
    def present_value(self, future_value, rate, time):
        '''
        Calculate present value.
        
        Args:
            future_value (float): The future value of money.
            rate (float): The discount rate (as a decimal).
            time (int): The time the money will be invested for (in years).
        
        Returns:
            float: The present value of money.
        '''
        return future_value / (1 + rate)**time
    
    def annuity_payment(self, present_value, rate, time):
        '''
        Calculate annuity payment.
        
        Args:
            present_value (float): The present value of money.
            rate (float): The discount rate (as a decimal).
            time (int): The number of periods over which the annuity will be paid.
        
        Returns:
            float: The periodic payment required.
        '''
        return present_value * (rate / (1 - (1 + rate)**-time))

        


# Example usage:
def main():
    calculator = FinanceCalculator()

    # User input Block #
    query_text = '''\nSelect which service you wish to use:
    [1] -- Calculate Compound interest
    [2] -- Calculate Simple interest
    [3] -- Calculate Present value
    [4] -- Calculate Annuity payment
    [5] -- Exit'''
    print('Welcome to the Finance Calculator!')
    name = input('Please enter your name: ')
    while True:
        choice = input(query_text + '\n\n' + 'Enter your choice: ')
        # exit program
        if choice == '5':
            print(f'Thank you {name} for using this financial service!\n\nYou have successfully exited the program.')
            break
        # error handling
        try:
            initial = float(input('Enter your initial amount: '))
            rate = float(input('Enter the annual interest rate as a decimal: '))
            time = float(input('Enter the years it will be invested for: '))
        except ValueError:
            print('Please enter numbers or decimal numbers only!')
        # if no exceptions, run the else block
        else:
            if choice == '1':
                print(f"\n{name} your Compound Interest:", calculator.compound_interest(initial, rate, time))
            elif choice == '2':
                print(f"\n{name} your Simple Interest:", calculator.simple_interest(initial, rate, time))
            elif choice == '3':
                print(f"\n{name} your Present Value:", calculator.present_value(initial, rate, time))
            elif choice == '4':
                print(f"\n{name} your Annuity Payment:", calculator.annuity_payment(initial, rate, time))



if __name__ == "__main__":
    main()