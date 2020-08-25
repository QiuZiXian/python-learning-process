from math import hypot


# The distance between 2 adjacent points in the grid,
# either horizontally or vertically, is considered to be 1.
# x coordinates are read horizontally, starting from 1,
#   increasing from left to right.
# y coordinates are read vertically, starting from 1,
#   increasing from top to bottom.
#
# The first point of a solution is to the left, or above, the second point
# of the solution.
#
# Solutions are printed from smallest to largest x coordinates,
# and for a given x coordinate, from smallest to largest y coordinates.
def f(grid):
    '''
    >>> f([[0, 0, 0],\
           [0, 0, 0]])
    The maximum distance between 2 points in the grid is 0
    That distance is between the following pairs of points:
    <BLANKLINE>
    >>> f([[0, 0, 1],\
           [0, 0, 0]])
    The maximum distance between 2 points in the grid is 0
    That distance is between the following pairs of points:
    <BLANKLINE>
    >>> f([[0, 0, 1],\
           [0, 0, 1]])
    The maximum distance between 2 points in the grid is 1.0
    That distance is between the following pairs of points:
    (3, 1) -- (3, 2)
    >>> f([[1, 0, 1],\
           [1, 0, 1]])
    The maximum distance between 2 points in the grid is 2.23606797749979
    That distance is between the following pairs of points:
    (1, 1) -- (3, 2)
    (3, 1) -- (1, 2)
    >>> f([[0, 0, 0, 0],\
           [0, 1, 0, 0],\
           [0, 0, 1, 0],\
           [0, 0, 0, 0],\
           [1, 1, 0, 0],\
           [1, 1, 0, 0]])
    The maximum distance between 2 points in the grid is 4.123105625617661
    That distance is between the following pairs of points:
    (2, 2) -- (1, 6)
    '''
    max_distance = 0
    # INSERT YOUR CODE HERE
    print('The maximum distance between 2 points in the grid is',
          max_distance
         )
    print("That distance is between the following pairs of points:")
    print()
    # REPLACE THE PRINT() STATEMENT ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest
    doctest.testmod()
