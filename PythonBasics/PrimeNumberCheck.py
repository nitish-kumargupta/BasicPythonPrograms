"""
Created on 24-Feb-2019
Author: Nitish Gupta

This module implements a simple logic for determining whether a given number is prime or not.

Test Steps followed:-

1. Prompt user for input number
2. Check if provided number is valid integer
3. If step 2 return True proceed with prime check otherwise return to step 1
4. Display result and exit
"""


class PrimeNumberCheck:
    '''class docstring'''
    
    def __init__(self):
        '''class initializer'''
        pass
        
    def testPrime(self):
        '''method for logic implementation'''
        num = self.userinput()
        for i in range(2, num):
            if (num % i == 0):
                print ("{0} is not a prime number".format(num))
                break
        else:
                print ("{0} is a prime number".format(num))    
    
    def userinput(self):
        '''prompt user for input'''
        try:
            num = int(input("Enter a number : "))
            if (num < 2):
                print ("Please enter number greater than 1 !!\nTry again..\n")
                return self.userinput()
        except ValueError as error:
            print ("Error msg:", error, "\nPlease enter valid number !!\nTry again..\n")
            return self.userinput()
        else:
            return num

        
if (__name__ == "__main__"):
    obj = PrimeNumberCheck()
    obj.testPrime()
