'''
factorial(3) = 3*2*1
factorial(3) = 3 * factorial(2)
factorial(2) = 2 * factorial(1)
factorial(1) = 1 * factorial(0)
factorial(0) = 1
factorial(n) = n * factorial(n-1)
'''


def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result

print(factorial(3))


'''
Output:

6
'''