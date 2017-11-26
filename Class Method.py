

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


    # class method
    @classmethod
    def set_raise_amt(cls, amount):     # note the use of 'cls' as the class variable. Use of 'class' is not allowed
                                        # since this is a reserved word
        cls.raise_amount = amount

emp1 = Employee('Stan','Corpuz', 100000)
emp2 = Employee('Mari','Corpuz', 200000)

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

Employee.set_raise_amt(1.05)    # calling the class method and passing 5%. Note only the percent amount is passed
                                # to the method


# example of use case where the string contains hyphen. One will need to parse the string
emp_string_1 = 'John-Doe-700000'
emp_string_2 = 'Mary-Joe-850000'
emp_string_3 = 'Peter-Manner-1000000'

# use of the 'split()' method
first, last, pay = emp_string_1.split('-')

# creates a new employee.
# there is better way to create a new employee by creating a new function within the class.
new_emp_1 = Employee(first, last, pay)

# prints out new employee
print("Name:",new_emp_1.fullname())
print("Email:",new_emp_1.email)
print("Salary:",new_emp_1.pay)

#
# # example of using the class variable and intance variable
# print("Use of Class variable",Employee.raise_amount)  # use of class variable (Employee)
# print("Use of intance variable for emp1",emp1.raise_amount)  # use of intance variable (emp1)
# print("Use of intance variable for emp1",emp2.raise_amount)     # use of intance variable (emp2)

#
# # here is a little trick to get the namespace for Class and Instance
# print(Employee.__dict__)    # note there is a variable called 'raise_amount'
# print()
# print(emp1.__dict__)    # note there is NO variable intance called 'raise_amount' in emp1


