'''
lst=[]
for x in range(1,11):
   lst.append(x**3)
print(lst)
'''
'''
Output:

[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
'''

#another method

lst=[]
lst=[x**3 for x in range(1,11)]
print(lst)


'''
Output:

[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
'''