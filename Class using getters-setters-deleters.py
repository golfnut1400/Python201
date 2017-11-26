
"""The property decorator allows us to define Class methods that we can access like attributes.
This allows us to implement getters, setters, and deleters.
"""

class Employee:

    #class variable
    raise_amount = 1.10   # set percent raise

    def __init__(self, first, last):
        self.first = first
        self.last = last


    # Use of property (@property) decorator. Allows to use the property to be use as a method but able to
    # access just like an attribute
    @property
    def email(self):     # note the use of 'self'
        return '{}{}.email.com'.format(self.first,self.last)

    # creates full name method within a class
    @property  # adding property decorator
    def fullname(self):     # note the use of 'self'
        return '{} {}'.format(self.first,self.last)

   # create a new employee using .setter
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # delete a new employee - use of deleter
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None



# create an employee object assigned to a variable emp_1
emp_1 = Employee('John','Smith')
emp_2 = Employee('Janet','Jackson')

#emp_1.first = 'Jim'
emp_1.fullname = 'Stan Corpuz'  # uses the @fullname.setter
emp_2.fullname = 'Mary Poppinns'

# print out of attributes of of the object
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)   # remove () from .fullname(). Using @property above (property decorator)
print()

print(emp_2.first)
print(emp_2.email)
print(emp_2.fullname)   # remove () from .fullname(). Using @property above (property decorator)


# delete an employee fullname
del emp_2.fullname

