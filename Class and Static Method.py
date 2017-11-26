import datetime

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

    # class method for parsing the string of new employees
    @classmethod
    def from_string(cls, emp_str):
        # use of the 'split()' method
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


    # Static method. Static method does not take a cls or self.
    @staticmethod
    def is_workday(date):
        if date.weekday() == 5 or date.weekday() == 6:  # 5 = Saturday; 6 = Sunday
            return False
        return True




emp1 = Employee('Stan','Corpuz', 100000)
emp2 = Employee('Mari','Corpuz', 200000)

#Variable use to pass to is_workday method
my_date = datetime.date(2017, 11, 23)

#calls the .is_workday function abve
print ("Is the date a workday?",Employee.is_workday(my_date))


