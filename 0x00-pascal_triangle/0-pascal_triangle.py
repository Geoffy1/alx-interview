#!/usr/bin/python3
'''A module for the Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a list of lists of int rep
    the Pascal's triangle of a given int.
    '''
    if n <= 0:
        return []
    triangle = [[1]*(a+1) for a in range(n)]
    for a in range(n):
        for j in range(1, a):
            triangle[a][j] = triangle[a-1][j-1] + triangle[a-1][j]
    return triangle
