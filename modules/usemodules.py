'''
Here I am importing some other module.
'''

import mymath
print(mymath.sum(10, 5))
print(mymath.diff(10, 5))

'''
output
15
5

'''


#another way to import the module

import mymath as ma
print(ma.sum(10, 5))
print(ma.diff(10, 5))

'''
output
15
5

'''

#one more way to import module


from mymath import *
print(sum(10, 5))
print(diff(10, 5))

'''
output
15
5

'''