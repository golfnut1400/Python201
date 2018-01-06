# use of inheritance


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

# Developer class inherits from the Employee class
class Developer(Employee):
    raise_amount = 1.20     # 20% increase in pay for a developer

    # creating to accept program language
    # use of the init to make use of the Employee class then adding additional parameters
    def __init__(self, first, last, pay, prog_lan, work_location):
        super().__init__(first, last, pay)  # inherit from the Employee class
        self.prog_lang = prog_lan   # add the program languge
        self.work_location = work_location # add the work location


# Manager class
# adding employess under the manager

class Manager(Employee):
    def __init__(self, first, last, pay, work_location,employees=None):
        super().__init__(first, last, pay)  # inherit from the Employee class
        self.work_location = work_location
        if employees is None:
            self.employees = []     # empty list
        else:
            self.employees = employees

    # ability for manager to add an employee in not in the list
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    # ability to remove and employee
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # prints out the employee of the manager
    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())




print()


dev1 = Developer('John','Smith', 100000, 'Python', 'UW Tower')    # data passed to the Developer class. If one would change Developer to
                                            # to Employee the raise_amount would be 10%
dev2 = Developer('Sara','Johns', 105000, 'Java', 'Facebook')
#
# print("Name:",dev1.fullname())
# print("Email:",dev1.email)
# print("Salary:",dev1.pay)
# print("Language:", dev1.prog_lang)
# print("Work Location:", dev1.work_location)

#   (first, last, pay, work location, employee)
mgr_1 = Manager('Sue','Black',90000, 'Amazon', [dev1])  # adds employee [dev1] to the mgr_1

# Add a new employee (dev2)to Manager
mgr_1.add_emp(dev2)

#remove dev1 employee
mgr_1.remove_emp(dev1)

# testing print
print(mgr_1.email)  #prints email
print(mgr_1.work_location)
mgr_1.print_emps() #print employees under this manager
print()

print("--- Here are uses of isinstance and issublcass---")
# Here is a great tool - isinstance
print("Is manager an instance of Employee?:",isinstance(Manager, Employee))
print("Is Employee an instance of Manager?:",isinstance(Employee, Manager))
print("Is Developer an instance of Employee?:",isinstance(Developer,Employee))
print("Is Developer an instance of Manager?:",isinstance(Developer, Manager))

print()
# Here is a great tool - issubclass
print("Is manager an subclass of Employee?:",issubclass(Manager, Employee))
print("Is Employee an subclass of Manager?:",issubclass(Employee, Manager))
print("Is Developer an subclass of Employee?:",issubclass(Developer,Employee))
print("Is Developer an subclass of Manager?:",issubclass(Developer, Manager))






#
# print()
# print("Amount BEFORE raise:",dev1.pay)
# (dev1.apply_raise())  # calls and applies raise
# print("Amount AFTER raise:",dev1.pay)

