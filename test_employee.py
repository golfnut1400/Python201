
"""
UNIT TESTING ------->
This unit test will use 'Employee.py file in the same file directory

Based off YouTube channel
by Corey Shaffer
Python Tutorial: Unit Testing Your Code with the unittest Module
https://www.youtube.com/watch?v=6tNS--WetLI

How to run in Terminal
1 - change directory to the location the test files are located (/PycharmProjects/Python201-EDx/Python201
2 - Type: python -m unittest test_employee


"""


import unittest
#import Employee
from Employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp1 = Employee('Stan','Corpuz', 100000)
        emp2 = Employee('Mari','Corpuz', 200000)

        self.assertEqual(emp1.email, 'Stan.Corpuz@company.com')
        self.assertEqual(emp2.email, 'Mari.Corpuz@company.com')

        emp1.first = 'John'
        emp2.first = 'Leslie'

        self.assertEqual(emp1.email, 'John.Corpuz@company.com')
        self.assertEqual(emp2.email, 'Leslie.Corpuz@company.com')

    # def test_fullname(self):
    #     emp1 = Employee('Stan','Corpuz', 100000)
    #     emp2 = Employee('Mari','Corpuz', 200000)
    #
    #     self.assertEqual(emp1.fullname, 'Stan','Corpuz')
    #     self.assertEqual(emp2.fullname, 'Mari','Corpuz')

        # self.assertEqual(emp1.fullname, 'Stan Corpuz')
        # self.assertEqual(emp2.fullname, 'Mari Corpuz')

        # emp1.first = 'John'
        # emp2.first = 'Leslie'
        #
        # self.assertEqual(emp1.fullname, 'John Corpuz')
        # self.assertEqual(emp2.fullname, 'Leslie Corpuz')



# this code below cannot be moved above the code above
# this allows to run the test in the PyCharm editor instead of going to the terminal.
# BTW... it will still work in the terminal by typing 'python test_calc.py'
if __name__ == '__main__':
    unittest.main()

