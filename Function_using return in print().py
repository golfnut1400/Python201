

# create and call make_doctor() with full_name argument from user input - then print the return value

def make_doctor(name):
    add_doctor = "Doctor "+name
    return add_doctor


full_name = input("What is your full name? ")

print(make_doctor(full_name))


""" ******************** """

# example of functions with return values used in functions
def msg_double(phrase):
      double = phrase + " " + phrase
      return double

# prints the returned object
print(msg_double("Save Now!"))

# echo the type of the returned object
type(msg_double("Save Now!"))

""" ******************** """

# [ ] add a 3rd period parameter to make_schedule
# [ ] Optional - print a schedule for 6 classes (Tip: perhaps let the function make this easy)
def make_schedule(period1, period2, period3):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title() + ", [3rd] " + period3.title())
    return schedule

student_schedule = make_schedule("mathematics", "history", "science")
print("SCHEDULE:", student_schedule)
