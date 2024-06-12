def calc(a,b):
    x=a+b
    y=a-b
    z=a*b
    u=a/b
    return x,y,z,u
result = calc(10,5)
print(result)


##Output (it will give the result based on the above function)
'''
Output:

(15, 5, 50, 2.0)
'''

#another way to print

def calc(a,b):
    x=a+b
    y=a-b
    z=a*b
    u=a/b
    return x,y,z,u
result = calc(10,5)
for i in result:print(i)

'''
Output:

15
5
50
2.0
'''