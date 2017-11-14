


def distance(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        dsquared = dx**2 + dy**2
        result = dsquared**0.5
        return result

def area(radius):
    b = 3.14159 * radius**2
    return b

def area2(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp) # function calling distance function
    result = area(radius)  # function calling area function. value from radius is
                                #passed onto area function
    return result

print(area2(0,0,1,1))
