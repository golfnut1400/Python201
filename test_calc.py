
"""
UNIT TESTING ------->
This unit test will use 'calc.py file in the same file directory

Based off YouTube channel
by Corey Shaffer
Python Tutorial: Unit Testing Your Code with the unittest Module
https://www.youtube.com/watch?v=6tNS--WetLI

How to run in Terminal
1 - change directory to the location the test files are located (/PycharmProjects/Python201-EDx/Python201
2 - Type: python -m unittest test_calc


Expectation:
....        # 4 dots
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK

Process finished with exit code 0

"""


import unittest
import calc   # this is the name of the module 'calc.py' being imported


class TestCalc(unittest.TestCase):

    def test_add(self):
        #result = calc.add(10, 5)    # calls add function from the calc module -
        self.assertEqual(calc.add(10, 5), 15, msg="Test")    # variable, 15 is the sum, msg is optional)
        self.assertEqual(calc.add(-1, 1), 0, msg="Test")     # check edge cases
        self.assertEqual(calc.add(-1, -1), -2, msg="Test")
    
    def test_subtract(self):
        #result = calc.subtract(10, 5)    # calls subtract function from the calc module -
        self.assertEqual(calc.subtract(10, 5), 5, msg="Test")
        self.assertEqual(calc.subtract(-1, 1), -2, msg="Test")
        self.assertEqual(calc.subtract(-1, -1), 0, msg="Test")
    
    def test_multiply(self):
        #result = calc.multiply(10, 5)    # calls multiply function from the calc module -
        self.assertEqual(calc.multiply(10, 5), 50, msg="Test")
        self.assertEqual(calc.multiply(-1, 1), -1, msg="Test")
        self.assertEqual(calc.multiply(-1, -1), 1, msg="Test")
    
    def test_divide(self):
        #result = calc.divide(10, 5)    # calls divide function from the calc module -
        self.assertEqual(calc.divide(10, 5), 2, msg="Test")
        self.assertEqual(calc.divide(-1, 1), -1, msg="Test")
        self.assertEqual(calc.divide(-1, -1), 1, msg="Test")
        #self.assertEqual(calc.divide(5, 2), 2.5, msg="Test")
    
    def test_add_add_divide(self):
        #result = calc.add_divide(10, 5)    # calls add_divide function from the calc module -
        self.assertEqual(calc.add_divide(10, 10, 2), 10, msg="Test")
        self.assertEqual(calc.add_divide(-1, 1, 2), 0, msg="Test")
        self.assertEqual(calc.add_divide(-1, -1, 2), -1, msg="Test")

        # testing exceptions - i.e. ValueError
        #self.assertRaises(ValueError, calc.divide, 10, 0)
                            # ValueError is the exception one will raise
                            # calc.divide is the filename.function. We however leave off the parenthesis. Arguments
                            #   are passed in separately
                            # 10, 0 are the test values. Will not raise the ValueError
                            # change 0 to 2 and run again. One will get the 'ValueError not raised by divide' error

        # here is better way to test the exceptions
        # we call the calc.divide() as we normally do with the arguments
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

# this code below cannot be moved above the code above
# this allows to run the test in the PyCharm editor instead of going to the terminal.
# BTW... it will still work in the terminal by typing 'python test_calc.py'
if __name__ == '__main__':
    unittest.main()


