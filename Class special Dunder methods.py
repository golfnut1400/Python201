# use of inheritance

# reference
# https://docs.python.org/3/reference/datamodel.html#special-method-names


class Employee:

    #class variable
    raise_amount = 1.10   # set to 0.4 percent

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email =  first + '.' + last + '@company.com'

    # creates full name method within a class
    def fullname(self):     # note the use of 'self'
        return '{} {}'.format(self.first,self.last)

    # Total pay after applying raise
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)   #need to add 'self' to use the instance
                                                   # or use Employee.raise_amount

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)


print()


emp_1 = Employee('John','Smith', 100000)    # data passed to the Developer class. If one would change Developer to
                                            # to Employee the raise_amount would be 10%
emp_2 = Employee('Sara','Johns', 105000)

print(emp_1)

# repr and str are used to display emp_1 object
print(repr(emp_1))
print(str(emp_1))
print()

# these will print the same way as above using the repr and str methods
print(emp_1.__str__())
print(emp_1.__repr__())
print()
# Another example
print("This will give the same results")
print(1 + 2)
print(int.__add__(1, 2))
print()

# dunder add string method example
print("Use of a dunder and string method")
print(str.__add__('Hello', ' World'))
print("Hello"+" World")
