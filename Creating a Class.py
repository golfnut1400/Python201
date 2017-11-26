
"""Part of a series for creating a class and instances
https://www.youtube.com/watch?v=ZDa-Z5JzLYM
"""


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



emp1 = Employee('Stan','Corpuz', 10000)
emp2 = Employee('Mari','Corpuz', 20000)

# print(emp1)     # note these are different objects in memory
# print(emp2)

# print(emp1.email)
# print(emp2.email)
#
# # priniting full name outside of the class
# print('{} {}'.format(emp1.first,emp1.last))
#
# # This will call the fullname function above in the Employee class
# print(emp1.fullname())
# print()
# # anther way to look at this by passing the arguments
# print(Employee.fullname(emp1))
# print()
#
# print("Emp1 is paid " +"$",emp1.pay)
#
# # example of using the class variable and intance variable
# print("Use of Class variable",Employee.raise_amount)  # use of class variable
# print("Use of intance variable",emp1.raise_amount)  # use of intance variable
# print(emp2.raise_amount)


# here is a little trick to get the namespace for Class and Instance
print(Employee.__dict__)    # note there is a variable called 'raise_amount'
print()
print(emp1.__dict__)    # note there is NO variable intance called 'raise_amount' in emp1


