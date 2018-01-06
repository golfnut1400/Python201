
"""UNIT TESTING ------->
This unit test will use 'test_employee.py file in the same file directory

Based off YouTube channel
by Corey Shaffer
Python Tutorial: Unit Testing Your Code with the unittest Module
https://www.youtube.com/watch?v=6tNS--WetLI

How to run in Terminal
1 - change directory to the location the test files are located (/PycharmProjects/Python201-EDx/Python201
2 - Type: python -m unittest test_employee"""



class Employee:

    #class variable
    raise_amount = 1.04   # set to 0.4 percent

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email =  first + '.' + last + '@company.com'

    # creates full name method within a class
    def fullname(self):     # note the use of 'self'
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self_pay = (self.pay * self.raise_amount)   #need to add 'self' to use the instance or use Employee.raise_amount


    # class method for setting the raise amount
    @classmethod
    def set_raise_amt(cls, amount):     # note the use of 'cls' as the class variable. Use of 'class' is not is not allowed
                                        # since this is a reserved word
        cls.raise_amount = amount



