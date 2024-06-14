a=[1,2,3,4,5]
b=[6,7,8,9,10]

z=[]
for i in range(len(a)):
    z.append(a[i]*b[i])
print(z)



'''
Output:

[6, 14, 24, 36, 50]
'''


#another way

a=[1,2,3,4,5]
b=[6,7,8,9,10]

z=[]
z=[a[i]*b[i] for i in range(len(a))]
print(z)


'''
Output:

[6, 14, 24, 36, 50]
'''
