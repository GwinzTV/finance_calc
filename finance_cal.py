class FinanceCalculator:
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

    # Calculate compound interest
    print("Compound Interest:", calculator.compound_interest(1000, 0.05, 5))

    # Calculate simple interest
    print("Simple Interest:", calculator.simple_interest(1000, 0.05, 5))

    # Calculate present value
    print("Present Value:", calculator.present_value(1000, 0.05, 5))

    # Calculate annuity payment
    print("Annuity Payment:", calculator.annuity_payment(1000, 0.05, 5))



if __name__ == "__main__":
    main()