a=[2,4,6,8]
b=[1,2,3,4]
result=[]

for i in a:
    if i in b:
        result.append(i)
print(result)

'''
Output:

[2, 4]
'''

#another way
a=[2,4,6,8]
b=[1,2,3,4]
result=[]

result=[i for i in a if i in b ]
print(result)


'''
Output:

[2, 4]
'''