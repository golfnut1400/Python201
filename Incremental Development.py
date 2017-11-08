

"""As an example, suppose you want to find the distance between two points, given by the coordinates (x1, y1) and (x2, y2).
By the Pythagorean theorem, the distance is:

Distance formula
"""

# Step 1. testing the smallest code for distance that takes for arguments

# def distance(x1, y1, x2, y2):
#     return 0.0

# Step 2. Call the function
def distance(x1, y1, x2, y2):
    return 0.0

print(distance(1, 2, 4, 6))


# Step 3
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return 0.0

# Step 4
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    return 0.0

# Step 5 final code
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**0.5
    return result

print(distance(1, 2, 4, 6))
