""""Based off YouTube channel
by Corey Shaffer
Python Tutorial: Unit Testing Your Code with the unittest Module
https://www.youtube.com/watch?v=6tNS--WetLI

I will be using test_calc.py to run unit testing"""




def add(x,y):
    """Add function"""
    return x + y

def subtract(x,y):
    """Subtract function"""
    return x - y


def multiply(x,y):
    """Multiply function"""
    return x * y

def divide(x,y):
    """divide function"""
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y

def add_divide(x,y,z):
    """add_divide function"""
    return (x + y) / z


