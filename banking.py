# -*- coding: utf-8 -*-
"""
Goblins Magical Loan System
A sophisticated system for approving loans to wizards starting businesses.

To test your current solution, run the `test_my_solution.py` file.

Refer to the instructions on Canavs for more information.

"I have neither given nor received help on this assignment."
author: Emma Choi
"""
__version__ = 4
import math

#(1) main: Calls the other functions and controls data flow
def main():
    '''
    Main function that calls all the other functions and provides
    an interactive loan processing experience.
        
    Args:
        None
    Returns:
        None
    '''
    # All functions are called in main
    print_introduction()
    name = input_name()
    rating = calculate_rating(name)
    print_rating(rating)
    loanAmount = input_loan_amount()
    print_loan_availability(rating, loanAmount)
    print_conclusion()

#(2) print_introduction: Print a welcome message
def print_introduction():
    '''
    print_introduction function prints a brief message that greets the user.
    It has no parameters and does not return anything.
        
    Args:
        None
    Returns:
        None
    '''
    print("* 1) Introduction ********************************")
    print("Welcome to the Goblins Magical Loan System!")
    print("Please answer the following questions truthfully,")
    print("and we will process your loan request.")
    print("Imposters will be fed to the dragons.")

#(3) input_name: Get the user's name
def input_name():
    '''
    input_name() function prompts the user to type in their name and prints
    it, as well as a few other messages. It has no parameters but returns the
    user's name as a string.
        
    Args:
        None
    Returns:
        str: name
    '''
    print("* 2) Name ****************************************")
    print("Please enter your full, legal name.")
    print("Magical verification will verify your identity.")
    name = input("Write your name and press enter: ")
    print("Welcome, " + name + "!")
    return name

#(4) calculate_rating: Get the user's rating (by Grindlehook)
# The following is Grindlehook's function. Do not modify it.
# You should not worry about HOW it works, but instead think of its
# arguments and return value. Remember you can only call it once!
# Do NOT change the following function definition
def calculate_rating(name):
    '''
    Returns the customer's credit rating, according to the bank's current
    status, the customer, and the alignment of the stars. This function
    is a little delicate, and will break after being called once.
    
    NOTE (ghook@1/15/2018): DO NOT TOUCH THIS, I FINALLY GOT IT WORKING.
    
    Returns:
        int: An integer (0-9) representing the customer's credit rating.
    '''
    c=calculate_rating;setattr(c,'r',lambda:setattr(c,'o',True))
    j={};y=j['CELESTIAL_NAVIGATION_CONSTANT']=10
    j[True]='CELESTIAL_NAVIGATION_CONSTANT'
    x=str(''[:].swapcase);y=y+11,y+9,y+-2,y+-2,y+4,y+-5,y+-1,y+11,y+9,\
    y+-6,y+-6,y+-1,y+-5,y+3,y+-7,y+7,y+-1,y+-5,y+8,y+-7,y+11,y+1
    z=lambda x,t,o=0:''.join(map(lambda j:x.__getitem__(j+o), t))
    if hasattr(c,'o')and not getattr(c, 'o'): return z(x,y)
    c.o=False;j['CELESTIAL_NAVIGATION_CONSTANT'].bit_length
    d=(lambda:(lambda:None))()();g=globals()
    while d:g['X567S-lumos-17-KLAUS']=((d)if(lambda:None)else(j))
    p=lambda p:sum(map(int, list(str(p))))
    MGC=p(sum(map(lambda v: v[0]*8+ord(v[1]), enumerate(name))))
    while MGC>10:MGC=p(MGC)
    if c:return MGC
# Do NOT change the preceding function definition
    
#(5) print_rating: Print the user's rating
def print_rating(rating):
    '''
    print_rating function prints the user's calculated rating, which is the
    result of calling the calculate_rating function. It takes in an integer,
    which is the rating, and does not return anything.
        
    Args:
        int: rating
    Returns:
        None
    '''
    print("* 3) Rating **************************************")
    print("Your user rating has been calculated.")
    print("Your rating is: " + (str)(rating) + "/10 points" )
    
#(6) input_loan_amount: Get the user's desired loan amount
def input_loan_amount():
    '''
    input_loan_amount function prompts the user to type in their desired loan
    amount and prints a few messages. It has no parameters, but returns the
    loan amount as an integer.
        
    Args:
        None
    Returns:
        int: loanAmount
    '''
    print("* 4) Loan ****************************************")
    print("Loans are made based on your customer rating.")
    print("However, you can request a loan of any size.")
    print("How many galleons do you want?")
    loanAmount = (int)(input("Write your loan amount: "))
    return loanAmount

#(7) print_loan_availability: Print whether the loan is available
def print_loan_availability(rating, loanAmount):
    '''
    print_loan_availability function takes in two parameters, a rating and a
    loanAmount. Using these, it prints whether or not a loan is available to
    the user by calling the test_loan function. It does not return anything.
        
    Args:
        int: rating
        int: loanAmount
    Returns:
        None
    '''
    availability = test_loan(rating, loanAmount)
    print("* 5) Available? **********************************")
    print("Your loan request has been evaluated.")
    print("Loan available:", availability)

#(8) test_loan: Determines if the loan is available
def test_loan(rating, loanAmount):
    '''
    test_loan function takes in two parameters, rating and loanAmount. It
    returns whether or not a loan is available to the user by using the
    formula: rating^2 * 100 >= loanAmount. A boolean is returned.
        
    Args:
        int: rating
        int: loanAmount
    Returns:
        bool: True or False
    '''
    return ((math.pow(rating, 2)) * 100 >= loanAmount)

#(9) print_conclusion: Prints a thank-you message.
def print_conclusion():
    '''
    print_conclusion function prints a brief message that thanks the user.
    It has no parameters and does not return anything.
        
    Args:
        None
    Returns:
        None
    '''
    print("* 6) Conclusion **********************************")
    print("Thanks for using Goblins Magical Loan System!")
    print("Best of luck with your new small business.")
    print("We hope you'll use Goblins for all your future")
    print("banking needs. Remember: Fortius Quo Fidelius!")
    print("**************************************************")

# Call main function only if this file is being run directly
#   as opposed to being run by `test_my_solution.py`
if __name__=='__main__':
    main()