def half(fun):
    def inner():
        n = fun()
        return n/2
    return inner
@half
def num():
    return 10


'''
Output

5.0
'''