#!/usr/bin/python3


"""
Defining a function for integer addition
"""


def add_integer(a, b=98):
    """to printinteger addition of teo numbers
    Args:
        a: (int/float)
        b: (int/float)pre-set to 98
    Raises:
        TypeError if a and b are not int or float
    Returns:
        the integer addition of a and b
    """
#    if (not(isinstance(a, int)
#            or isinstance(a, float))):
#        raise TypeError("a must be an integer")
#    if (not(isinstance(b, int) or
#            isinstance(b, float))):
#        raise TypeError("b must be an integer")
#    return (int(a) + int(b))

    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        a = int(a)
        b = int(b)


        try:
            result = a + b
            print(result)
        except TypeError:
            raise TypeError("a must be an integer or b must be an integer")
    else:
        raise TypeError("a must be an integer or b must be an integer")

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
