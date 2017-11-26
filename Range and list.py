

# example of the use of range and setting output to a list

x = range(0,100,5)   # range(start, end, [step]
y = list(x)         # setting output into a list
print(y)

print()
x = range(100,0,-5)   # range(start, end, [step]
y = list(x)         # setting output into a list
print(y)

print()
x = range(0,- 100,- 5)   # range(start, end, [step]
y = list(x)         # setting output into a list
print(y)
print(type(y))
