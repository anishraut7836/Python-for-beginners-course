def myfun(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)

myfun(10, 20, name="Anish", sal=111111)



'''
Output:

10
(20,)
{'name': 'Anish', 'sal': 111111}

'''