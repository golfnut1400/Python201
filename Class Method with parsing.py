

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
    def set_raise_amt(cls, amount):     # note the use of 'cls' as the class variable. Use of 'class' is not is
                                        # not allowed since this is a reserved word
        cls.raise_amount = amount

    # class method for parsing the string of new employees
    @classmethod
    def from_string(cls, emp_str):
        # use of the 'split()' method.
        first, last, pay = emp_string_1.split('-')  # removes the hyphen
        return cls(first, last, pay)


# creates an Employee object and assigns to variable
emp1 = Employee('Stan','Corpuz', 100000)
emp2 = Employee('Mari','Corpuz', 200000)


Employee.set_raise_amt(1.05)    # calling the class method and passing 5%. Note only the percent amount is passed
                                # to the method


# example of use case where the string contains hyphen. One will need to parse the string
emp_string_1 = 'John-Doe-700000'
emp_string_2 = 'Mary-Joe-850000'
emp_string_3 = 'Peter-Manner-1000000'

# creates a new employee by passing the variable to class method (.from_string)above
new_emp_1 = Employee.from_string(emp_string_1)

# prints out new employee
print("Name:",new_emp_1.fullname())
print("Email:",new_emp_1.email)
print("Salary:",new_emp_1.pay)
