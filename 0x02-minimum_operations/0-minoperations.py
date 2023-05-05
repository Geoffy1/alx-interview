#!/usr/bin/python3
'''Creates the minimum operations
'''


def minOperations(n):
    '''Computes the fewest no of operations needed to result
    in exact n H characters.
    '''
    if n == 1:
        return 0
    
    operations = 0
    copied = 1
    
    while copied < n:
        if n % copied == 0:
            operations += 1
            copied *= n // copied
        else:
            operations += 1
            copied += copied
    
    if copied == n:
        return operations
    else:
        return 0
