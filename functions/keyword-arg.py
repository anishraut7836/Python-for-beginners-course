def average(a,b):
    print(a)
    print(b)
    return (a+b)/2
print(average(b=10,a=20))


'''
Output:

20
10
15.0
'''

def average(a=10,b=20):
    print(a)
    print(b)
    return (a+b)/2
print(average(b=30))

