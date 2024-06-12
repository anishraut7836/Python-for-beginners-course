x=123

def dispaly():
    x=678
    print(x)

print(x)
dispaly()


'''
#It will print local variable and as well global variable

Output:

123
678
'''


#another way to print global variable

x=123

def dispaly():
    x=678
    print(x)
    print(globals()['x'])

print(x)
dispaly()


'''
Output:

123
678
123
'''


#assign function to a variable

x=123

def dispaly():
    x=678
    print(x)
    print(globals()['x'])

print(x)
z = dispaly
z()
z()
z()