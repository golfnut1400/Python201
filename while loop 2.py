

def number(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    while n != 1:
        print(n)
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    print(n)                  # the last print is 1

number(100) # try changing value and see what happens
